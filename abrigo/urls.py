from django.urls import path
from .views import AbrigosView, AbrigoAddView, AbrigoUpdateView, AbrigoDeleteView

urlpatterns = [
    path('abrigos/', AbrigosView.as_view(), name='abrigos'),
    path('abrigo/adicionar/', AbrigoAddView.as_view(), name='abrigo_adicionar'),
    path('<int:pk>/abrigo/editar/', AbrigoUpdateView.as_view(), name='abrigo_editar'),
    path('<int:pk>/abrigo/apagar/', AbrigoDeleteView.as_view(), name='abrigo_apagar'),
]
