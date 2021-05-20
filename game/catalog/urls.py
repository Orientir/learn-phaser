from django.contrib import admin
from django.urls import path, include

from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('first-game', views.first_game, name='first-game'),
    path('space-shooter', views.space_shooter, name='space-shooter'),
]