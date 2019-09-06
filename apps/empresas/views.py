from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import Empresa


class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome',]

    def form_valid(self, form):
        # Instancia um objeto form dentro da variavel obj
        obj = form.save()
        #atribuo a variavel usuario o usuario logado
        funcionario = self.request.user.funcionario
        #digo ao obj(form.save()) que atribua esta empresa ao  model funcionario.empresa
        funcionario.empresa = obj
        #Salve neste funcionario a empresa que acabei de criar
        funcionario.save()
        #retorna alguma coisa
        return HttpResponse('OK!!!')


class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nome', ]

