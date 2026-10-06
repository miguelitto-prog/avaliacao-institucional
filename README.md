# avaliacao-institucional

Trabalho de Lab. Programação Back End - API em Django onde alunos avaliam disciplinas.

## Como rodar

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Rotas

- /admin/
- /api/alunos/
- /api/disciplinas/
- /api/avaliacoes/
- /api/avaliacoes/pendentes/
- /api/avaliacoes/resumo/

## Perguntas

### 1. Por que usamos um ambiente virtual em cada projeto?

(sua resposta)

### 2. Por que dividimos o sistema em 3 apps em vez de um só?

(sua resposta)

### 3. Para que servem makemigrations e migrate, e por que nessa ordem?

(sua resposta)
