from django.urls import path
from .views import DepartamentoViews, DepartamentoNovo, DepartamentoEdit, DepartamentoDelete

urlpatterns = [
    path('', DepartamentoViews.as_view(), name='list_departamentos'),
    path('novo/', DepartamentoNovo.as_view(), name='novo_departamento'),
    path('edit/<int:pk>/', DepartamentoEdit.as_view(), name='edit_departamento'),
    path('delete/<int:pk>/', DepartamentoDelete.as_view(), name='delete_departamento'),
]
