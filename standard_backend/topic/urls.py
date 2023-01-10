from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.topic_list),
    path('<int:pk>/', views.topic_detail)
    ]