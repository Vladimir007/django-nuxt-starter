from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import UserChangeForm, UserCreationForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    list_display = ("email", "full_name", "is_active", "is_staff", "is_superuser")
    list_filter = ("email", "first_name", "last_name", "is_active", "is_staff", "is_superuser")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
    )
    add_fieldsets = ((None, {"fields": ("email", "first_name", "last_name", "password1", "password2")}),)
    search_fields = ("email",)
    ordering = ("email",)

    @admin.display(description='Name')
    def full_name(self, obj):
        return f"{obj.last_name} {obj.first_name}"


admin.site.register(User, CustomUserAdmin)
