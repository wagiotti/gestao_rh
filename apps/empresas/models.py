from django.db import models


class Empresa(models.Model):
    nome = models.CharField(max_length=200, help_text="Nome da empresa")

    def __str(self):
        return self.nome

