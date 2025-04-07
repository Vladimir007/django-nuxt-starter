from django.contrib.auth.forms import UserChangeForm as DjangoUserChangeForm, BaseUserCreationForm

from .models import User


class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")


class UserChangeForm(DjangoUserChangeForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")
