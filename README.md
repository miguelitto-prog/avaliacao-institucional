# avaliacao-institucional

API em Django de um sistema de **avaliação institucional**, em que alunos avaliam as disciplinas que cursam.
Atividade prática da disciplina **Lab. Programação Back End** – Universidade de Vassouras.

## Estrutura

```
avaliacao-institucional/
├── .gitignore
├── README.md
└── backend/
    ├── manage.py
    ├── requirements.txt
    ├── config/          # projeto (settings e urls principais)
    ├── alunos/          # model Aluno
    ├── disciplinas/     # model Disciplina
    └── avaliacoes/      # model Avaliacao (ForeignKey para Aluno e Disciplina)
```

## Como rodar o projeto

```bash
# 1. Clonar o repositório
git clone https://github.com/SEU-USUARIO/avaliacao-institucional.git
cd avaliacao-institucional/backend

# 2. Criar e ativar o ambiente virtual
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 3. Instalar as dependências
pip install -r requirements.txt

# 4. Criar o banco de dados
python manage.py migrate

# 5. Criar o superusuário (para acessar o Admin)
python manage.py createsuperuser

# 6. Subir o servidor
python manage.py runserver
```

Admin: http://127.0.0.1:8000/admin/

## Rotas da API

| Rota | O que devolve |
|---|---|
| `/api/alunos/` | Todos os alunos |
| `/api/disciplinas/` | Todas as disciplinas |
| `/api/avaliacoes/` | Todas as avaliações |
| `/api/avaliacoes/pendentes/` | Só as avaliações com status PENDENTE |
| `/api/avaliacoes/resumo/` | (Desafio 1) Média das notas e total de avaliações RESPONDIDAS por disciplina |

## Perguntas

### 1. Por que usamos um ambiente virtual em cada projeto?

O venv é tipo uma "caixinha" só desse projeto, onde ficam as bibliotecas que ele usa. Se eu instalasse tudo direto no Python do computador, um projeto que precisa do Django 4 ia brigar com outro que precisa do Django 5. Com um venv por projeto, cada um tem as suas versões e um não atrapalha o outro. Além disso, junto com o `requirements.txt`, qualquer pessoa consegue recriar exatamente o mesmo ambiente em outra máquina, sem precisar subir a pasta `venv/` pro GitHub.

### 2. Por que dividimos o sistema em 3 apps em vez de um só?

Porque cada parte cuida de um assunto diferente: `alunos` cuida de quem avalia, `disciplinas` do que é avaliado e `avaliacoes` liga os dois. Separando, o código fica mais organizado e fácil de achar as coisas, cada app tem seus próprios models, views e urls, e se um dia precisar mexer só nas disciplinas, mexo só naquele app. Também dá pra reaproveitar um app em outro projeto (por exemplo, o app de alunos num sistema de matrícula).

### 3. Para que servem makemigrations e migrate, e por que nessa ordem?

O `makemigrations` olha os models que eu escrevi e gera um arquivo (a migration) dizendo o que mudou: "criar a tabela Aluno", "adicionar o campo nota", etc. É como escrever a receita. O `migrate` pega essas receitas e aplica de verdade no banco de dados, criando ou alterando as tabelas. A ordem é essa porque o `migrate` só aplica o que já existe em migration: se eu rodar ele antes do `makemigrations`, o Django não sabe que eu mudei o model e o banco fica desatualizado.
