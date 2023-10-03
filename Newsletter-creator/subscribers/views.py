from django.http import HttpResponse
from django.shortcuts import render
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from PIL import Image

from .forms import SubscribeForm, UnsubscribeForm
from .models import Subscriber
from .tokens import account_activation_token
from news.models import NewsLetter
from utility import send_utility 


def add_subscriber(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subscriber = form.save(commit=False)
            form.save()
            
            # Send Confirmation Email
            send_utility.send_confirmation_mail(request, subscriber)

            return render(request, 'subscribers/subscription_confirm.html', locals())
    else:
        form = SubscribeForm()
    previous_newsletters = NewsLetter.objects.filter(published=True).order_by('-published_date')
    
    context = {
        'form': form,
        'previous_newsletters': previous_newsletters,
    }
    return render(request, 'subscribers/add_subscriber.html', locals())


def confirm_subscriber(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        subscriber = Subscriber.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Subscriber.DoesNotExist):
        subscriber = None

    if subscriber is not None and account_activation_token.check_token(subscriber, token):
        subscriber.confirmed = True
        subscriber.save()
    else:
        return HttpResponse('Something went wrong, please try again')

    return render(request, 'subscribers/subscription_complete.html', {'subscriber': subscriber})


def unsubscribe(request):
    if request.method == 'POST':
        form = UnsubscribeForm(request.POST)
        if form.is_valid():
            unsubcriber = form.save(commit=False)
            subscriber = Subscriber.objects.get(email=unsubcriber.email)
            unsubcriber.first_name = subscriber.first_name
            unsubcriber.last_name = subscriber.last_name
            unsubcriber.delivered_emails = subscriber.delivered_emails
            unsubcriber.opened_emails = subscriber.opened_emails
            unsubcriber.save()
            subscriber.delete()
            
            return render(request, 'subscribers/unsubscribe_complete.html', locals())
    else:
        form = UnsubscribeForm()

    return render(request, 'subscribers/unsubscribe.html', locals())


# For tracking if user opens email
def image_load(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        subscriber = Subscriber.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Subscriber.DoesNotExist):
        subscriber = None

    if subscriber is not None and account_activation_token.check_token(subscriber, token):
        subscriber.opened_emails += 1
        subscriber.save()
        red = Image.new('RGB', (1, 1))
        response = HttpResponse(content_type='image/png')
        red.save(response, 'PNG')
        return response
    else:
        return HttpResponse('Something went wrong')
