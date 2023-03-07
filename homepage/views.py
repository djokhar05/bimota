from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from clothe.models import Clothe

# Create your views here.


def home_page(requests):
    context = Clothe.objects.all()
    # context = Clothe.objects.filter(cloth_gender="unisex")
    print(context)
    return render(requests, 'homepage/home_page.html', {"clothes": context})
