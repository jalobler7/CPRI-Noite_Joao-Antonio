from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.views.generic.base import TemplateResponseMixin
from django.views import View


from .forms import VoluntarioModelForm
from .models import Voluntario

class VoluntariosView(ListView):
    model = Voluntario
    template_name = 'voluntarios.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(VoluntariosView, self).get_queryset()

        if buscar:
            return qs.filter(nome__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 1)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            messages.info(self.request, 'Não existem voluntários cadastrados')
            return qs


class VoluntarioAddView(SuccessMessageMixin, CreateView):
    model = Voluntario
    form_class = VoluntarioModelForm
    template_name = 'voluntario_form.html'
    success_url = reverse_lazy('voluntarios')
    success_message = 'Voluntário cadastrado com sucesso'


class VoluntarioUpdateView(SuccessMessageMixin, UpdateView):
    model = Voluntario
    form_class = VoluntarioModelForm
    template_name = 'voluntario_form.html'
    success_url = reverse_lazy('voluntarios')
    success_message = 'Voluntário atualizado com sucesso'


class VoluntarioDeleteView(SuccessMessageMixin, DeleteView):
    model = Voluntario
    template_name = 'voluntario_apagar.html'
    success_url = reverse_lazy('voluntarios')
    success_message = 'Voluntário deletado com sucesso'


# VoluntariosAbrigoInLine = inlineformset_factory(
#     Voluntario,
#     VoluntariosAbrigo,
#     fk_name='voluntario',  # Define a chave estrangeira correta para Voluntario
#     fields=('abrigo',),  # Ajuste os campos conforme necessário
#     extra=1,
#     can_delete=True
# )

# class VoluntarioInLineEditView(TemplateResponseMixin, View):
#     template_name = 'voluntario_form_inline.html'
#
#     def get_formset(self, data=None):
#         return VoluntariosAbrigoInLine(instance=self.voluntario, data=data)
#
#     def dispatch(self, request, pk):
#         self.voluntario = get_object_or_404(Voluntario, id=pk)
#         return super().dispatch(request, pk)
#
#     def get(self, request, *args, **kwargs):
#         formset = self.get_formset()
#         return self.render_to_response({'voluntario': self.voluntario, 'formset': formset})
#
#     def post(self, request, *args, **kwargs):
#         formset = self.get_formset(data=request.POST)
#         if formset.is_valid():
#             formset.save()
#             return redirect('voluntarios')  # Redireciona para a lista de voluntários após salvar
#         return self.render_to_response({'voluntario': self.voluntario, 'formset': formset})