from django.urls import path
from . import views

urlpatterns = [
    path('music/', views.music, name='music'),
    path('music/player/', views.player, name='player'),

    path('record/', views.record, name='record'),
]