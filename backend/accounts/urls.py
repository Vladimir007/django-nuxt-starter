from django.urls import path

from accounts import views

urlpatterns = [
    path('account/', views.AccountViewSet.as_view()),
    path('login/', views.Login.as_view()),
    path('logout/', views.Logout.as_view()),
    path('test/', views.Test.as_view()),
]
