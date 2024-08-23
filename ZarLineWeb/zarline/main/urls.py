from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path("ZarLine's prospects", views.prospects, name='prospects'),
    path("ZarLine's contacts", views.contacts, name='contacts')
]
