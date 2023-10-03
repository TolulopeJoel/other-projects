from django.db import models


class Subscriber(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(blank=True, max_length=25)
    email = models.EmailField(unique=True)

    confirmed = models.BooleanField(default=False)  # True if subscriber confirms email
    
    delivered_emails = models.IntegerField(default=0)
    opened_emails = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Unsubscriber(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(blank=True, max_length=25)
    email = models.EmailField(unique=True)
    
    delivered_emails = models.IntegerField(default=0)
    opened_emails = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email