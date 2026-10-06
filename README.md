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

Pra cada projeto ter as suas próprias bibliotecas. Se eu instalar tudo no computador direto, um projeto pode precisar de uma versão do Django e outro de outra, e aí dá conflito. Com o venv cada um fica separado. E como o venv não vai pro GitHub, o requirements.txt serve pra instalar tudo de novo em outra máquina.

### 2. Por que dividimos o sistema em 3 apps em vez de um só?

Porque cada app cuida de uma coisa: alunos é quem avalia, disciplinas é o que é avaliado e avaliacoes junta os dois. Fica mais organizado, cada um tem seus models, views e urls, e se precisar mudar algo em disciplinas por exemplo, mexo só nesse app.

### 3. Para que servem makemigrations e migrate, e por que nessa ordem?

O makemigrations olha os models e cria um arquivo com as mudanças que precisam ser feitas no banco. O migrate pega esse arquivo e aplica no banco de verdade, criando as tabelas. Tem que ser nessa ordem porque se rodar o migrate antes, ainda não tem nenhuma migration nova pra ele aplicar.
