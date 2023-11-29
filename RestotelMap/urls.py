from django.urls import path
from django.views.generic.base import RedirectView
from .views import *
from . import views

app_name = 'RestotelMap'

urlpatterns = [
    path('', views.accueil, name = 'accueil'),
]
