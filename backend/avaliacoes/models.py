from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from alunos.models import Aluno
from disciplinas.models import Disciplina


class Avaliacao(models.Model):
    STATUS_PENDENTE = "PENDENTE"
    STATUS_RESPONDIDA = "RESPONDIDA"
    STATUS_CHOICES = [
        (STATUS_PENDENTE, "Pendente"),
        (STATUS_RESPONDIDA, "Respondida"),
    ]

    nota = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    comentario = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=STATUS_PENDENTE,
    )
    data_criacao = models.DateTimeField(auto_now_add=True)

    # A ForeignKey fica aqui (e não no Aluno) porque um aluno faz VÁRIAS
    # avaliações. Se ficasse no Aluno, ele só poderia apontar para uma.
    # Relação 1:N -> 1 aluno para N avaliações.
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name="avaliacoes",
    )

    # A ForeignKey fica aqui (e não na Disciplina) porque uma disciplina
    # recebe VÁRIAS avaliações. Cada avaliação aponta para a sua disciplina.
    # Relação 1:N -> 1 disciplina para N avaliações.
    disciplina = models.ForeignKey(
        Disciplina,
        on_delete=models.CASCADE,
        related_name="avaliacoes",
    )

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"

    def __str__(self):
        return f"{self.aluno.nome} -> {self.disciplina.codigo} ({self.status})"
