from django.contrib import admin

from .models import Disciplina


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nome", "professor", "periodo")
    search_fields = ("nome", "codigo", "professor")
