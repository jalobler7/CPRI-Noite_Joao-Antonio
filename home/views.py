#from tempfile import template
from django.shortcuts import render
#from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name= 'principal.html'

def pagina_inicial(request):
    return render(request, 'principal.html')