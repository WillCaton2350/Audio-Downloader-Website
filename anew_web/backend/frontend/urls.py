from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index.html'),
    path('index.html',views.index,name='index.html'),
    path('about.html',views.about,name='about.html'),
    path('contact.html',views.contact,name='contact.html')
]