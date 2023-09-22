from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

# Пример представлений для аутентификации
class MyLoginView(LoginView):
    template_name = 'login.html'
    # Другие настройки

class MyLogoutView(LogoutView):
    template_name = 'logout.html'
    # Другие настройки

class MyPasswordChangeView(PasswordChangeView):
    template_name = 'change_password.html'
    # Другие настройки
