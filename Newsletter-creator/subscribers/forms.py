from django import forms

from .models import Subscriber, Unsubscriber

my_default_errors = {}

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control w-50'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control w-50'}),
            'email': forms.TextInput(attrs={'class': 'form-control w-50'}),
        }
        my_default_errors['unique'] = 'You subscribed sometime ago'
        error_messages = {
            'email': my_default_errors,
        }


class UnsubscribeForm(forms.ModelForm):
    class Meta:
        model = Unsubscriber
        fields = ('email',)
        
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control w-50',}),
        }
        my_default_errors['unique'] = 'You are not a subscriber, suubscribe to unsubscribe'
        error_messages = {
            'email': my_default_errors,
        }