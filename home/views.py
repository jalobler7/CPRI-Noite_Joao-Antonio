from django.views.generic import TemplateView
from django.shortcuts import redirect

class IndexView(TemplateView):
    template_name = 'principal.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:  # Se o usuário não estiver logado
            return redirect('login')  # Redireciona para a página de login
        return super().dispatch(request, *args, **kwargs)
