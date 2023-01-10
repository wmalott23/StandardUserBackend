from django.urls import path
from . import views

urlpatterns = [
    path('', views.thread_list),
    path('<int:pk>/', views.thread_detail),
    ]