from django.urls import path

from . import views

urlpatterns = [
    path('contact', views.contact, name='contact.html'),
    path('',views.index, name='index.html')
    
]
