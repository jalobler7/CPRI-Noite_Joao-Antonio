from django.urls import path
from .views import DoacoesView, DoacaoAddView, DoacaoUpdateView, DoacaoDeleteView

urlpatterns = [
    path('doacoes/', DoacoesView.as_view(), name='doacoes'),
    path('doacoes/adicionar/', DoacaoAddView.as_view(), name='doacoes_adicionar'),
    path('<int:pk>/doacoes/editar/', DoacaoUpdateView.as_view(), name='doacoes_editar'),
    path('<int:pk>/doacoes/apagar/', DoacaoDeleteView.as_view(), name='doacoes_apagar'),
]
