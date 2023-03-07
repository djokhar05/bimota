from django.shortcuts import render

# Create your views here.


def AboutView(requests):
    return render(requests, 'about/about.html')
