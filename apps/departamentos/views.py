from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Departamento


class DepartamentoViews(ListView):
    model = Departamento
    fields = ['nome',]

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = Departamento.objects.filter(empresa=empresa_logada)
        return queryset


class DepartamentoNovo(CreateView):
    model = Departamento
    fields = ['nome',]

    def form_valid(self, form):
        departamento = form.save(commit = False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentoNovo, self).form_valid(form)


class DepartamentoEdit(UpdateView):
    model = Departamento
    fields = ['nome',]


class DepartamentoDelete(DeleteView):
    model = Departamento
    fields = ['nome',]
    success_url = reverse_lazy('list_departamentos')