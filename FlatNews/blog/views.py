# from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from .forms import EmailPostForm, CommentForm, SearchForm
from django.views.generic import ListView
from django.shortcuts import render
from .models import Post


# Template Views

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/post_list.html'


# def post_list(request, tag_slug=None):
#     object_list = Post.published.all()
#     tag = None

#     #  tags
#     from taggit.models import Tag
#     if tag_slug:
#         tag = get_object_or_404(Tag, slug=tag_slug)
#         object_list = object_list.filter(tags__in=[tag])

#     #  paginator
#     from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#     paginator = Paginator(object_list, 10)
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)

#     context = {'posts': posts, 'page': page, 'tag': tag}
#     return render(request, 'blog/post/post_list.html', context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', published_date__year=year,
                             published_date__month=month, published_date__day=day)

    #  comments
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    #  list of similar posts
    from django.db.models import Count
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-published_date')[:4]

    context = {'post': post, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form,
               'similar_posts': similar_posts}
    return render(request, 'blog/post/post_detail.html', context)


# Forms views


def share_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    mail_is_sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{user['name']} recommends you read  {post.title}"
            message = f"Read the post '{post.title}' at {post_url}\n\n {user['name']}\'s comment {user['comments']}"
            send_mail(subject, message, user['email'], [
                user['to']], fail_silently=False)
            mail_is_sent = True
    else:
        form = EmailPostForm()
        user = EmailPostForm()

    context = {'post': post, 'form': form,
               'mail_is_sent': mail_is_sent, 'user': user}
    return render(request, 'blog/post/share.html', context)


def show_latest_posts(request):
    count = 5
    latest_posts = Post.published.order_by('-published_date')[:count]

    context = {'latest_posts': latest_posts}
    return render(request, 'blog/post/latest_posts.html', context)


def post_search(request):
    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector(
                'title', weight='A') + SearchVector('content', weight='B')
            search_query = SearchQuery(query)
            results = Post.published.annotate(search=search_vector, rank=SearchRank(
                search_vector, search_query)).filter(rank__gte=0.2).order_by('-rank')

    context = {'form': form, 'query': query, 'results': results}
    return render(request, 'blog/post/search.html', context)
