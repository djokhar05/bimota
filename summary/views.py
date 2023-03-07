from django.shortcuts import render

# Create your views here.


def summaryView(request):
    return render(request, "summary/summary.html")
