# <img src="https://valora.cc/img/logo2.png" alt="Valora" width="24" /> Desafio Backend Python

## Modelagem do banco

![](modelage-desafio-backend.jpg)

## Tasklist

- [X] Implementar modelo de user personalizado
- [X] Criar models conforme modelagem
- [X] Implementação da autenticação JWT
- [X] CRUD Usuários
- [X] CRUD Categoria
- [X] CRUD Questões
- [X] Implementação do QUIZ
- [X] Implementação dos filtros do Rank


## Endpoints.

**User**:
*http://127.0.0.1:8000/api/users/register/
> Endpoint para registro de usuários.

* http://127.0.0.1:8000/api/users/login/
> Passando email e senha, assim você obterá seu token de acesso.

* http://127.0.0.1:8000/api/users/
> Listagem geral dos usuários.

* http://127.0.0.1:8000/api/users/profile/
> Perfil simples do usuário que fez a requisição.

* http://127.0.0.1:8000/api/users/update/:id/
> Alteração do perfil do usuário passando o ID, endpoint aguarda os fields: name, email e is_admin(Booleano)

* http://127.0.0.1:8000/api/users/delete/:id/
> Desativação do usuário, como boa prática acredito que nenhuma informação seja excluída apenas desativa.


## Download & Instruções para instalação.

* 1 - Clone o projeto: git clone https://github.com/JonathaCnB/desafio-backend.git
* 2 - cd desafio-backend
* 3 - Criar virtual environment: python -m venv venv
* 4 - venv\scripts\activate
* 5 - pip install -r requirements.txt
* 6 - python manage.py migrate
* 7 - python manage.py createsuperuser
* 8 - python manage.py runserver