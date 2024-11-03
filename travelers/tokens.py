from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type

class TokenRegenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user: AbstractBaseUser, timestamp: int) -> text_type:
        return (
            text_type(user.pk) + text_type(timestamp) 
        )

token = TokenRegenerator()