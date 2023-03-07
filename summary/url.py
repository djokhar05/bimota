from django.urls import path
from . import views


urlpatterns = [
    path('', views.summaryView, name="summary"),
]
