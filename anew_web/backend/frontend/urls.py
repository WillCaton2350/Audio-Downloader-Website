from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index.html'),
    path('index.html',views.index,name='index.html'),
    path('drums.html',views.drums,name='drums.html'),
    path('bass.html',views.bass,name='bass.html'),
    path('vox.html',views.vox,name='vox.html')
]