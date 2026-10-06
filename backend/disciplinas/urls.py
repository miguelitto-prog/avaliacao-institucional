from django.urls import path

from . import views

urlpatterns = [
    path("", views.listar_disciplinas, name="listar_disciplinas"),
]
