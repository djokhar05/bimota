from django.shortcuts import render

# Create your views here.


def checkOutView(request):
    return render(request, "checkout/checkout.html")
