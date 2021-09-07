# <img src="https://valora.cc/img/logo2.png" alt="Valora" width="24" /> Desafio Backend Python

## Modelagem do banco

![](modelage-desafio-backend.jpg)

## Download & Instruções para instalação.

* 1 - Clone o projeto: git clone https://github.com/JonathaCnB/desafio-backend.git
* 2 - cd desafio-backend
* 3 - Criar virtual environment: python -m venv venv
* 4 - venv\scripts\activate
* 5 - pip install -r requirements.txt
* 6 - python manage.py migrate
* 7 - python manage.py createsuperuser
* 8 - python manage.py runserver

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

* http://127.0.0.1:8000/api/users/register/
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

**Categorias**:

* http://127.0.0.1:8000/api/questions/categories/
> Listagem das categorias cadastradas, se filtrado pelo admin busca todas, caso contrario busca apenas as ativas.

* http://127.0.0.1:8000/api/questions/create-category/
> Criação de uma nova categoria, aguarda o field name.

* http://127.0.0.1:8000/api/questions/update-category/:id/
> Atualização de uma categoria existente, aguarda o parâmetro pk e field name.

* http://127.0.0.1:8000/api/questions/delete-category/:id/
> Desativação de uma categoria existente, aguarda o parâmetro pk.

**Perguntas**:

* http://127.0.0.1:8000/api/questions/
> Listagem das perguntas cadastradas.

* http://127.0.0.1:8000/api/questions/create/
> Criação de uma nova pergunta, aguarda os fields: question, first_answer, second_answer, third_answer, correct_answer(1, 2 ou 3) e category(id).

* http://127.0.0.1:8000/api/questions/update/:id/
> Atualização de uma pergunta existente, aguarda o parâmetro pk e os fields: question, first_answer, second_answer, third_answer, correct_answer(1, 2 ou 3) e category(id).

* http://127.0.0.1:8000/api/questions/delete/:id/
> Desativação de uma pergunta existente, aguarda o parâmetro pk.

**Quiz**:

* http://127.0.0.1:8000/api/questions/quiz/
> Para jogar acesse o endpoint acima que listara as categorias.

* http://127.0.0.1:8000/api/questions/quiz/:id/
> Apos a categoria selecionada, passa para esse segundo endpoint com o parâmetro pk da categoria, **esse endpoint lhe retornará as 10 questões aleatórias**.

* http://127.0.0.1:8000/api/questions/quiz-answers/
> Por fim use esse endpoint para responder as questões, passando no form-data o id da pergunta e resposta.

**Rank**:

* http://127.0.0.1:8000/api/rank/
> Listagem dos quizzes respondidos.

* http://127.0.0.1:8000/api/rank/user/
> Pontuação do usuário que chamou o endpoint.

* http://127.0.0.1:8000/api/rank/user/:id/
> Pontuação do usuário por categoria, endpoint requer o pk da categoria.

**Conclusão**:

Faltaram alguns pontos como uma regra para só liberar as categorias que tiverem mais de 10 perguntas, e com o rank faltou a listagem por usuário e pontuação.


## Agradecimentos

Quero agradecer essa oportunidade de participar deste processo seletivo. Indiferente do resultado, considerando tecnicamente o antes e depois, eu aprendi muito com esse desafio. Essa é a questão, estudar sem nenhum propósito, é decorar um monte de regras sem saber se um dia vai usar. Estudar com um propósito, isso sim é gratificante. Obrigado a todos.