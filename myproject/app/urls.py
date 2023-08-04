from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import  settings

from .views import *
from . import views
from . import views



urlpatterns = [
    
    path('', views.index, name='index'),         # URL for index.html
    path('family/', views.family, name='family'), # URL for family.html
    path('upload/', upload,name='upload'),
    path('retrieve/', retrieve,name='retrieve'),
    path('about/', about,name='about'),
    path('contact/', views.contact, name='contact'),

    path('family/', family,name='family'),
    path('base/', base,name='base'),
    path('child/', child,name='child'),
    
]



urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)