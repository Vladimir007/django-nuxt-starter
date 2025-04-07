from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator, classonlymethod
from django.views.decorators.csrf import ensure_csrf_cookie

from django_q.tasks import async_task

from rest_framework.exceptions import ValidationError
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import User
from .serializers import UserSerializer
from .tasks import test_task


class AccountViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return super().get_permissions()

    def get_object(self):
        return self.request.user

    @classonlymethod
    def as_view(cls):
        return super().as_view(actions={
            'get': 'retrieve',
            'post': 'create',
            'patch': 'partial_update',
        })


@method_decorator(ensure_csrf_cookie, name="dispatch")
class Login(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, **kwargs):
        # Just set CSRF cookie
        return Response({})

    def post(self, request, **kwargs):
        email, password = request.data.get('email'), request.data.get('password')
        if not email or not password:
            raise ValidationError({"detail": "Please enter both email and password"})
        user = authenticate(email=email, password=password)
        if user is None:
            raise ValidationError({"detail": "Invalid credentials"})
        login(request, user)

        serializer = UserSerializer(instance=user)
        return Response(serializer.data)


class Logout(APIView):
    def post(self, request, **kwargs):
        logout(request)
        return Response({})


class Test(APIView):
    def post(self, request, **kwargs):
        async_task(test_task, request.user, task_name="Test API")
        return Response({'detail': "Test response"})
