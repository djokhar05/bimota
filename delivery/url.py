from django.urls import path
from . import views


urlpatterns = [
    path('', views.DeliveryFormView.as_view(), name="delivery"),
    path('order_complete/<int:pk>', views.OrderCompleted, name="order_complete"),
]
