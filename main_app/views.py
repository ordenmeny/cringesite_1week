from django.shortcuts import render
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "main_app/index.html"
    extra_context = {'title': 'Главная страница'}

