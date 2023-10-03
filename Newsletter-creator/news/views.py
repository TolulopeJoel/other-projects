import calendar
from datetime import date

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.text import slugify
from django.views import generic
from django.views.decorators.http import require_POST

from .forms import NewsLetterForm, PostForm
from .models import NewsLetter, Post
from subscribers.models import Subscriber, Unsubscriber
from utility import send_utility


# Post
class CreatePost(LoginRequiredMixin, generic.CreateView):
    form_class = PostForm
    template_name = 'news/create_post.html'
    success_url = reverse_lazy('news:post_list')

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


class PostList(LoginRequiredMixin, generic.ListView):
    model = Post
    context_object_name = 'posts'


class PostDetail(LoginRequiredMixin, generic.DetailView):
    model = Post
    slug_field = 'slug'
    context_object_name = 'post'


# News Letter
@login_required
def newsboard(request):
    return render(request, 'news/newsboard.html', {})

@login_required
def metrics(request):
    # Percentage of subscribers to unsubscribers
    subscribers = Subscriber.objects.filter(confirmed=True)
    subs_count =  len(subscribers)

    unsubscribers = Unsubscriber.objects.all()
    unsubs_count = len(unsubscribers)

    total_user_count = subs_count + unsubs_count
    subscribers_percent =  round((subs_count / total_user_count) * 100, 2)
    unsubscribers_percent = round((unsubs_count / total_user_count) * 100, 2)

    now = timezone.now()
    today = now.replace(hour=0, minute=0, second=0, microsecond=0)

    # Monthly subscribers  
    months_name = [month.lower() for month in calendar.month_name]
    months_name.remove('')

    monthly_subscribers = {}
    for index, month_name in enumerate(months_name):
        month = today.replace(month=index + 1, day=1)
        if month.month == 12:
            next_month = today.replace(year=today.year + 1, month=1, day=1)
        else:
            next_month = today.replace(month=month.month + 1, day=1)
        monthly_subscribers[month_name] = Subscriber.objects.filter(confirmed=True, created_at__gte=month).exclude(created_at__gte=next_month)

    # Percentage of read and unread emails
    sent_emails = 0
    read_emails = 0
    for subscriber in subscribers:
        sent_emails += subscriber.delivered_emails
        read_emails += subscriber.opened_emails
    unread_emails = sent_emails - read_emails

    read_emails_percent = round((read_emails / sent_emails) * 100, 2)
    unread_emails_percent =  round((unread_emails / sent_emails) * 100, 2)

    return render(request, 'news/metrics.html', locals())


class CreateLetter(LoginRequiredMixin, generic.CreateView):
    form_class = NewsLetterForm
    template_name = 'news/create_letter.html'
    success_url = reverse_lazy('news:letter_list')

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


class NewsLetterList(LoginRequiredMixin, generic.ListView):
    model = NewsLetter
    context_object_name = 'news'


class PreviousNewsLetterList(generic.ListView):
    model = NewsLetter
    template_name = 'news/previous_newsletters.html'
    context_object_name = 'previous_newsletters'

    def get_queryset(self):
        return super().get_queryset().filter(published=True).order_by('-published_date')


class DraftNewsLetterDetail(LoginRequiredMixin, generic.DetailView):
    queryset = NewsLetter.objects.filter(published=False)
    slug_field = 'slug'
    context_object_name = 'news'

class PublishedNewsLetterDetail(generic.DetailView):
    queryset = NewsLetter.objects.filter(published=True)
    slug_field = 'slug'
    context_object_name = 'news'


@require_POST
def send_newsletter(request, pk):
    send_utility.send_news_letter(request, pk)
    return redirect('news:newsboard')
