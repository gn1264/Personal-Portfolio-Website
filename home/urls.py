# home/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # root path
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
    path('about/', views.about, name='about'),
]
