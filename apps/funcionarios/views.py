from django.views.generic import ListView, UpdateView
from .models import Funcionario


class FuncionariosList(ListView):
    model = Funcionario
    #Faz com que o funcionario veja dados somente da sua empresa
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = Funcionario.objects.filter(empresa=empresa_logada)
        return queryset



class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome','departamentos',]

