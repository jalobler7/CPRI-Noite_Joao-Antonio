from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail

from django.core.paginator import Paginator
from django.shortcuts import redirect, get_object_or_404
from django.template.loader import render_to_string

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages


from .forms import VoluntarioModelForm
from .models import Voluntario


class VoluntarioExibir(DetailView):
    model = Voluntario
    template_name = 'voluntario_exibir.html'


    def get_object(self, queryset=None):

        voluntario = get_object_or_404(Voluntario, pk=self.kwargs.get('pk'))


        self.enviar_email(voluntario)
        messages.success(self.request, "E-mail de confirmação enviado com sucesso!")

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

        #messages.success(self.request, message="E-mail enviado para o voluntário!")



class VoluntariosView(ListView):
    model = Voluntario
    template_name = 'voluntarios.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(VoluntariosView, self).get_queryset()

        if buscar:
            return qs.filter(nome__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 5)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            messages.info(self.request, 'Não existem voluntários cadastrados')
            return qs
        #self.enviar_email(voluntarios,abrigo)

# def enviar_email(self, voluntarios):
    #     email = [voluntarios.email]
    #     dados = {
    #         'voluntario': voluntarios,
    #         'abrigo': voluntarios.abrigo,
    #     }
    #
    #     texto_email = render_to_string('emails/texto_email.txt', dados)
    #     html_email = render_to_string('emails/texto_email.html', dados)
    #     send_mail(
    #         subject='Lavacar-Serviço Concluído',
    #         message=texto_email,
    #         from_email='jalobler0107@gmail.com',
    #         recipient_list=email,
    #         html_message=html_email,
    #         fail_silently=False,
    #     )
    #
    #     return redirect('voluntarios')



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


