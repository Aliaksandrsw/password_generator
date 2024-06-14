from django.urls import path
from . import views

urlpatterns = [
    path('', views.PasswordGeneratorView.as_view(), name='password_gen'),
    path('send-password-email/', views.SendPasswordEmailView.as_view(), name='send_password_email'),
]
