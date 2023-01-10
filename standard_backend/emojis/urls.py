from django.urls import path
from . import views

urlpatterns = [
    path('', views.emoji_list),
    path('<int:pk>/', views.emoji_detail),
    ]