from django.shortcuts import render
from django.views import generic, View


class HomePage(generic.TemplateView):
    template_name = 'index.html'
