## Descrição
- Este projeto tem fim avaliativo para o processo seletivo de desenvolvedor backend python da empresa Valora.
- Foi desenvolvida uma API para uma aplicação para a criação de um quiz de perguntas e respostas.
- Abaixo pode ser visualizado um diagrama simples das pastas e arquivos do projeto:

  - desafio-backend
    - app
      - accounts
        - tests
          - test_accounts_model.py
          - test_accounts_views.py
        - __init__.py
        - admin.py
        - apps.py
        - forms.py
        - managers.py
        - models.py
        - serializers.py
        - urls.py
        - views.py
      - app
        - __init__.py
        - settings.py
        - urls.py
        - wsgi.py
      - quiz
        - tests
          - test_quiz_models.py
          - test_quiz_views.py
        - __init__.py
        - admin.py
        - apps.py
        - models.py
        - serializers.py
        - urls.py
        - views.py
      db.sqlite3
      manage.py
      pytest.ini
   docker-compose.yml
   Dockerfile
   exemplos_de_utilizacao.postman_collection.json
   LICENSE
   README.md
   requirements.txt
    
  
## Tecnologias Utilizadas
Nesse projeto foi utilizado as seguintes tecnologias:

* **Python**
* **Django**
* **Django REST Framework**
* **Pytest**
* **Docker**

## Bibliotecas Utilizadas

* Django==2.2.13
* django-extensions==2.0.7
* djangorestframework==3.9.1
* django-cors-headers==3.6.0
* django-rest-knox==4.1.0
* django-nested-admin==3.3.3
* pytest-django==4.1.0

OBS: A biblioteca django-rest-knox é a única que não era requisito para o desafio.
- Vantagens da escolha da biblioteca django-rest-knox em comparação com a autenticação do DRF integrado.
  - O Knox fornece um token por chamada para a visualização de login - permitindo que cada cliente tenha seu próprio token, que é excluído no lado do servidor quando o cliente efetua logout.
  - O Knox também oferece uma opção para um cliente conectado remover todos os tokens que o servidor possui - forçando todos os clientes a se autenticarem novamente.
  - Os tokens DRF são armazenados sem criptografia no banco de dados. Isso permitiria a um invasor acesso irrestrito a uma conta com um token se o banco de dados fosse comprometido.
  - Os tokens Knox são armazenados apenas de forma criptografada. Mesmo se o banco de dados fosse roubado de alguma forma, um invasor não seria capaz de fazer login com as credenciais roubadas.
  - Os tokens DRF rastreiam seu tempo de criação, mas não têm nenhum mecanismo embutido para a expiração dos tokens. Os tokens Knox podem ter uma expiração definida nas configurações do aplicativo (o padrão é 10 horas).

- Link de referência das vantagens do knox: https://pypi.org/project/django-rest-knox/

## Features Implementadas

As seguintes features foram implementadas:

### Como Administrador
* Adicionar/Atualizar/Deletar questionários e todos os outros cadastros oriundos de ações do player.

### Como Player
* Registrar ou logar com nome de usuário e senha.
* Listar todos os questinários cadastrados.
* Visualizar perguntas e opções de respostas para um determinado questionário.
* Enviar resposta para uma determinada questão de um respectivo questionário.
* Listar o desempenho para todos os questionários respondidos.
* Visualizar ranking geral por quiz.
* Visualizar ranking por categoria.

## Endpoints
* Player Create
  - Description: Endpoint para criação de um novo player.
  - Method: POST
  - URL: http://0.0.0.0:8000/accounts/create/
  - Body:
    - Format: json
    - { "username" : " ", "password": " "}
    
* Player Login
  - Description: Endpoint para login de um respectivo player.
  - Method: POST
  - URL: http://0.0.0.0:8000/accounts/login/
  - Body:
    - Format: json
    - { "username" : " ", "password": " "}  

* List Quizzes
  - Description: Endpoint para visualizar todos os questionários cadastrados no sistema.
  - Method: GET
  - URL: http://0.0.0.0:8000/quiz/quizzes/
  - Headers:
    - Authorization: Token *Insira o token*

* View Questions
  - Description: Endpoint para visualizar todas as questões e suas respectivas opções de respostas para um determinado questionário.
  - Method: GET
  - URL: http://0.0.0.0:8000/quiz/quizzes/${slug-quiz}$/
  - Headers:
    - Authorization: Token *Insira o token*
    
* Submit Answers
  - Description: Endpoint para envio da resposta escolhida pelo player para uma determinada questão de um quiz.
  - Method: POST
  - URL: http://0.0.0.0:8000/quiz/quizzes/submit/${slug-quiz}$/
  - Body:
    - Format: json
    - { "question" : "", "answer": " "}
    - OBS: question e answer devem ser os ids da questão a ser respondida e a resposta escolhida pelo player, respectivamente.
  - Headers:
    - Authorization: Token *Insira o token*

* My Results
  - Description: Endpoint para o player visualizar todos os questionários participados por ele e seus respectivos scores.
  - Method: GET
  - URL: http://0.0.0.0:8000/quiz/player-quizzes/
  - Headers:
    - Authorization: Token *Insira o token*
 
* Ranking by Quiz
  - Description: Endpoint para visualização do ranking geral por questionário.
  - Method: GET
  - URL: http://0.0.0.0:8000/quiz/ranking/${slug-quiz}$/
  - Headers:
    - Authorization: Token *Insira o token*
 
* Ranking by Category
  - Description: Endpoint para visualização do ranking por categoria.
  - Method: GET
  - URL: http://0.0.0.0:8000/quiz/ranking/category/
  - Headers:
    - Authorization: Token *Insira o token*
    - Category: *Insira a categoria para criação do ranking*

* OBS: Todos os endpoints testados e com exemplos podem ser acessados através da coleção criada no Postman. A coleção pode ser acessada na raiz deste diretório com o nome "exemplos_de_utilizacao.postman_collection.json"

## Tests

- Os testes implementados podem ser acessados na pasta "Tests" de cada aplicação, ou seja, existe uma pasta "Tests" para a aplicação "quiz" e uma para a aplicação "accounts".
Foram testados os models e as conexões com os endpoints.
- OBS: Não foram testadas as conexões com os endpoints de _method_ POST, por eu não conseguir encontrar esta informação em tempo hábil na documentação da biblioteca.

Para executar os testes:
```bash
$ docker-compose run app pytest
```

