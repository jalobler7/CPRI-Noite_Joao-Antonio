from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages


from .forms import VoluntarioModelForm
from .models import Voluntario


class VoluntarioExibir(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Voluntario
    template_name = 'voluntario_exibir.html'
    permission_required = 'voluntarios.view_voluntario'
    permission_denied_message = 'Listar Voluntarios'


    def get_object(self, queryset=None):

        voluntario = get_object_or_404(Voluntario, pk=self.kwargs.get('pk'))


        self.enviar_email(voluntario)
        return voluntario

    def enviar_email(self, voluntario):

        email = []
        email.append(voluntario.email)
        dados = {
            'voluntario': voluntario,
            'abrigo': voluntario.abrigo
        }

        texto_email = render_to_string('emails/texto_email.txt', dados)
        html_email = render_to_string('emails/texto_email.html', dados)

        send_mail(
            subject='Confirmação de Alocação no Abrigo',
            message=texto_email,
            from_email='jalobler0107@gmail.com',
            recipient_list=email,
            html_message=html_email,
            fail_silently=False,
        )




class VoluntariosView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'voluntarios.view_voluntario'
    permission_denied_message = 'Listar Voluntarios'
    model = Voluntario
    template_name = 'voluntarios.html'
    paginate_by = 5



    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(VoluntariosView, self).get_queryset()

        if buscar:
            return qs.filter(Q(nome__icontains=buscar) | Q(cpf__icontains=buscar))

        else:
            messages.info(self.request, 'Não existem voluntários cadastrados')
            return qs




class VoluntarioAddView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Voluntario
    form_class = VoluntarioModelForm
    template_name = 'voluntario_form.html'
    success_url = reverse_lazy('voluntarios')
    success_message = 'Voluntário cadastrado com sucesso'
    permission_required = 'voluntarios.add_voluntario'
    permission_denied_message = 'Adcionar Voluntarios'




class VoluntarioUpdateView(LoginRequiredMixin,PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Voluntario
    form_class = VoluntarioModelForm
    template_name = 'voluntario_form.html'
    success_url = reverse_lazy('voluntarios')
    success_message = 'Voluntário atualizado com sucesso'
    permission_required = 'voluntarios.change_voluntario'
    permission_denied_message = 'Editar Voluntarios'


class VoluntarioDeleteView(PermissionRequiredMixin,SuccessMessageMixin, DeleteView):
    model = Voluntario
    template_name = 'voluntario_apagar.html'
    success_url = reverse_lazy('voluntarios')
    success_message = 'Voluntário deletado com sucesso'
    permission_required = 'voluntarios.delete_voluntario'
    permission_denied_message = 'Deletar Voluntarios'


