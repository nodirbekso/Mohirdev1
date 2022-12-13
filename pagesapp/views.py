from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'
class AboutPageView(TemplateView):
    template_name = 'about.html'
class SomsaPageView(TemplateView):
    template_name = 'somsa.html'
class MontiPageView(TemplateView):
    template_name = 'monti.html'
