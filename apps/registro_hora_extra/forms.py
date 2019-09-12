from django.forms import ModelForm
from .models import Registro_hora_extra
from apps.funcionarios.models import Funcionario


class RegistroHoraExtraForm(ModelForm):
    """ Sobrescrevendo o metodo __init__ para filtrar os funcionarios somente da empresa que pertence """
    def __init__(self, user, *args, **kwargs):
        super(RegistroHoraExtraForm, self).__init__(*args, **kwargs)
        self.fields['funcionario'].queryset = Funcionario.objects.filter(empresa = user.funcionario.empresa)

    class Meta:
        model = Registro_hora_extra
        fields = ['motivo','funcionario','horas']