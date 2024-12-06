from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


class RegisterUserView(CreateView):
    template_name = "users/signup.html"
    form_class = UserCreationForm
    extra_context = {"title": "Регистрация"}

    def get_success_url(self):
        return reverse_lazy("main_app:home_page")


class LoginUser(LoginView):
    template_name = "users/login.html"
    extra_context = {"title": "Войти"}
