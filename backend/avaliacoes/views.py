from django.db.models import Avg, Count
from django.http import JsonResponse

from .models import Avaliacao


def listar_avaliacoes(request):
    avaliacoes = Avaliacao.objects.all()
    return JsonResponse(list(avaliacoes.values()), safe=False)


def listar_pendentes(request):
    pendentes = Avaliacao.objects.filter(status="PENDENTE")
    return JsonResponse(list(pendentes.values()), safe=False)


# Desafio 1: para cada disciplina, média das notas e total de
# avaliações RESPONDIDAS.
def resumo_por_disciplina(request):
    resumo = (
        Avaliacao.objects.filter(status="RESPONDIDA")
        .values("disciplina__id", "disciplina__codigo", "disciplina__nome")
        .annotate(media_notas=Avg("nota"), total_respondidas=Count("id"))
        .order_by("disciplina__codigo")
    )
    dados = []
    for item in resumo:
        media = item["media_notas"]
        dados.append({
            "disciplina_id": item["disciplina__id"],
            "codigo": item["disciplina__codigo"],
            "nome": item["disciplina__nome"],
            "media_notas": round(media, 2) if media is not None else None,
            "total_respondidas": item["total_respondidas"],
        })
    return JsonResponse(dados, safe=False)
