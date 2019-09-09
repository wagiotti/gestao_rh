from django.urls import path, include
from .views import FuncionariosList, FuncionarioEdit, FuncionarioDelete, FuncionarioNovo

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('editar/<int:pk>/', FuncionarioEdit.as_view(), name='update_funcionarios'),
    path('novo/', FuncionarioNovo.as_view(), name='create_funcionarios'),
    path('deletar/<int:pk>/', FuncionarioDelete.as_view(), name='delete_funcionarios'),
]
