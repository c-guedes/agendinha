from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.

from .models import Pessoa,Agenda


class HomePageView(ListView):
    model = Agenda
    template_name = 'agendita/home.html'


