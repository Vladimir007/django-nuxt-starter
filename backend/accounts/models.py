from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class User(AbstractUser):
    REQUIRED_FIELDS = ['first_name', 'last_name']
    USERNAME_FIELD = 'email'

    username = None
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(_("first name"), max_length=150)
    last_name = models.CharField(_("last name"), max_length=150)

    is_active = models.BooleanField(_("active"), default=False, help_text=_(
        "Designates whether this user should be treated as active. Unselect this instead of deleting accounts."
    ))

    objects = CustomUserManager()

    class Meta:
        swappable = 'AUTH_USER_MODEL'
        db_table = 'accounts'
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.email
