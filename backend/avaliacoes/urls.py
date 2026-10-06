from django.urls import path

from . import views

urlpatterns = [
    path("", views.listar_avaliacoes, name="listar_avaliacoes"),
    path("pendentes/", views.listar_pendentes, name="listar_pendentes"),
    path("resumo/", views.resumo_por_disciplina, name="resumo_por_disciplina"),
]
