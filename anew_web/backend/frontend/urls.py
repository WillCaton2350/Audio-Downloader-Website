from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index.html'),
    path('index.html',views.index,name='index.html'),
    path('drums.html',views.drums,name='drums.html'),
    path('bass.html',views.bass,name='bass.html'),
    path('vox.html',views.vox,name='vox.html'),
    path('play_audio/', views.play_audio, name='play_audio'),
    path('play_laidback/',views.play_laidback,name="play_laidback"),
    path('afrobeat/',views.afrobeat,name="afrobeat"),
    path('pandas/',views.pandas,name="pandas"),
    path('tera/',views.tera,name="tera"),
    path('Beregin/',views.Beregin,name="Beregin")
]