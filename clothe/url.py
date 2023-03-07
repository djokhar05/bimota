from django.urls import path
from . import views


urlpatterns = [
    path('', views.ClotheListView.as_view(), name="clothe_list"),
    path('<slug:slug>', views.ClotheListView.as_view(),
         name="clothe_list_category"),
    path('<int:pk>/', views.ClotheDetailView.as_view(), name="clothe_detail")
]
