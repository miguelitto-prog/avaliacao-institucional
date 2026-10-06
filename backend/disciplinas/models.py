from django.db import models


class Disciplina(models.Model):
    nome = models.CharField(max_length=150)
    codigo = models.CharField(max_length=20, unique=True)
    professor = models.CharField(max_length=150)
    periodo = models.CharField(max_length=10)  # ex.: 2026.2

    def __str__(self):
        return f"{self.codigo} - {self.nome}"
