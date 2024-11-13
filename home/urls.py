from operator import index

from django.contrib import admin
from django.urls import path, include
from .views  import IndexView, render, TemplateView
from . import views

urlpatterns = [
    path('', IndexView.as_view(), name = 'index'),
    path('', views.pagina_inicial, name='pagina_inicial')
]
