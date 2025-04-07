from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        if self.instance:
            if attrs.get('password1') != attrs.get('password2'):
                raise ValidationError({"password2": _("Passwords didn't match.")})
            attrs.pop('password2', None)
        elif attrs['password1'] != attrs['password2']:
            raise ValidationError({"password2": _("Passwords didn't match.")})

        return attrs

    def create(self, validated_data):
        return self.Meta.model.objects.create_user(
            validated_data['email'],
            validated_data['first_name'],
            validated_data['last_name'],
            password=validated_data['password1'],
        )

    def update(self, instance, validated_data):
        password = validated_data.pop('password1', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'is_staff',
            'password1',
            'password2',
        )
        extra_kwargs = {
            'is_staff': {'read_only': True},
        }
