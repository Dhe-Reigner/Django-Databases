from django.urls import path
from .import views

urlpatterns = [
    path('', views.home,name='home.html'),
    path('join/', views.join,name='join.html'),
]