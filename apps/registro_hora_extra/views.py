from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from apps.registro_hora_extra.forms import RegistroHoraExtraForm
from .models import Registro_hora_extra


class HoraExtraList(ListView):
    model = Registro_hora_extra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Registro_hora_extra.objects.filter(funcionario__empresa = empresa_logada)


class HoraExtraEdit(UpdateView):
    model = Registro_hora_extra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraDelete(DeleteView):
    model = Registro_hora_extra
    success_url = reverse_lazy('list_hora_extra')


class HoraExtraCreate(CreateView):
    model = Registro_hora_extra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraCreate, self).get_form_kwargs()
        kwargs.update({'user':self.request.user})
        return kwargs


