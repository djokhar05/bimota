from django.urls import path
from . import views


urlpatterns = [
    path('', views.checkOutView, name="checkout"),
]
