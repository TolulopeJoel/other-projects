import datetime
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import timezone
from django.utils.encoding import force_bytes
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode

from news.models import NewsLetter
from subscribers.models import Subscriber, Unsubscriber
from subscribers.tokens import account_activation_token


def send_confirmation_mail(request, subscriber):
    """
    Send confirmation mail after user
    subscribes to newsletter.
    """
    email_context = {
        'subscriber': subscriber,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(subscriber.pk)),
        'token': account_activation_token.make_token(subscriber),
        'protocol': 'https' if request.is_secure() else 'http',
    }
    
    html_content = render_to_string('emails/confirm_subscription.html', email_context)
    plain_text_content = strip_tags(html_content)

    send_mail(
        'Subscription confirmation',
        plain_text_content,
        settings.DEFAULT_FROM_EMAIL,
        [subscriber.email],
        html_message=html_content,
        fail_silently=False,
    )
    subscriber = Subscriber.objects.get(email=subscriber.email)
    subscriber.delivered_emails += 1
    subscriber.save()


def send_news_letter(request, pk):
    news = NewsLetter.objects.get(id=pk)
    posts = news.posts.all()
    subscribers = Subscriber.objects.filter(confirmed=True)

    try:
        for subscriber in subscribers:
            subscriber = subscriber
            email_context = {
                'news': news,
                'posts': posts,
                'newsletter_link': request.build_absolute_uri(
                    reverse('news:letter_detail', args=[news.slug])
                ),
                'subscriber': subscriber,
                'domain': get_current_site(request).domain,
                'uid': urlsafe_base64_encode(force_bytes(subscriber.pk)),
                'token': account_activation_token.make_token(subscriber),
                'protocol': 'https' if request.is_secure() else 'http',
            }

            html_content = render_to_string('news/newsletter_detail.html', email_context)
            plain_text_content = strip_tags(html_content)

            send_mail(
                news.title,
                plain_text_content,
                settings.DEFAULT_FROM_EMAIL,
                [subscriber.email],
                html_message=html_content,
                fail_silently=False,
            )
            subscriber.delivered_emails += 1
            subscriber.save()

        news.published = True
        news.published_date = timezone.now()
        news.save()

        for post in posts:
            post.status = 'published'
            post.save()

    except:
        pass


def send_re_engagement_mail(request):
    """
    Send a re-engagement email after users
    have unsubscribed for more than a month
    but less than two months.
    """
    today = timezone.now()
    one_month = today - datetime.timedelta(days=30)
    two_month = today - datetime.timedelta(days=60)
    unsubscribers = Unsubscriber.objects.filter(created_at__lte=one_month)
    unsubscribers = unsubscribers.exclude(created_at__lte=two_month)
    html_content = render_to_string('emails/re_engagement.html', {})
    plain_text_content = strip_tags(html_content)

    send_mail(
        'Re-engagement Mail',
        plain_text_content,
        settings.DEFAULT_FROM_EMAIL,
        [unsubscriber.email for unsubscriber in unsubscribers],
        html_message=html_content,
        fail_silently=False,
    )
