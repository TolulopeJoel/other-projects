from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six  

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, subscriber, timestamp):
        return (
            six.text_type(subscriber.pk) + six.text_type(timestamp)
        )

account_activation_token = AccountActivationTokenGenerator()