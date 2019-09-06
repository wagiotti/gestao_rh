from django.urls import path, include
from .views import EmpresaCreate, EmpresaEdit


urlpatterns = [
    path('novo', EmpresaCreate.as_view(), name='create_empresa'),
    path('edit/<int:pk>/', EmpresaEdit.as_view(), name='edit_empresa'),

]
