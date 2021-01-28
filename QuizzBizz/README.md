## <img src="https://valora.cc/img/logo2.png" alt="Valora" width="24" /> Desafio Backend Python

Parabéns! Se você chegou até aqui significa que você passou pelas etapas mais difíceis do nosso processo seletivo. Somos extremamente criteriosos com as pessoas que vão integrar nosso time porque só aceitamos pessoas incríveis!

Agora é a parte fácil. Chegou a hora de mostrar todas as suas habilidades de transformar café em código. Vamos lá?

Nesse desafio iremos avaliar suas habilidades em:

* **Python**
* **Django**
* **Django REST Framework**
* **Pytest**
* **Docker**

Você irá desenvolver a API de uma aplicação para a criação de um quiz de perguntas e respostas!

**A aplicação deverá prover o registro e autenticação de dois tipos de usuários**:

* Admin
* Player

**Cada quiz é composto por**:

* 10 perguntas com 3 respostas onde apenas 1 é correta.
* Cada resposta correta acumula a 1 ponto.
* Cada resposta errada perde 1 ponto. A menor pontuação possível é 0.
* Possui uma categoria.

**Ao iniciar o jogo**:

* O player deve escolher uma categoria válida e receber um quiz com perguntas aleatórias referentes a categoria escolhida.

**Ao finalizar o jogo**:

* O player deve receber a contabilização dos seus pontos juntamente com a sua posição atual no ranking global. Não há limitação de quantos quizzes o player pode responder.

**O ranking global**:

* É a contabilização dos pontos acumulados por cada player.
* Ranking geral considera todas as categorias.
* Ranking por categoria agrupa por categorias.

**Permissões**:

* Todos os endpoints devem estar protegidos por autenticação.
* Usuários do tipo **Admin** tem permissão para criar perguntas e respostas para os quizzes.
* Usuários do tipo **Player** tem permissão para jogar e consultar o ranking.

## Requisitos

* O projeto precisa estar configurado para rodar em um ambiente macOS ou Ubuntu (preferencialmente como container Docker).
* Deve anexar ao seu projeto uma coleção do postman com todos os endpoints criados e exemplos de utilização.

**Para executar seu código devemos executar apenas os seguintes comandos**:

* git clone $seu-fork
* cd $seu-fork
* comando para instalar dependências
* comando para executar a aplicação

## Critério de avaliação

* **Organização do código**: Separação de módulos, view e model
* **Clareza**: O README explica de forma resumida qual é o problema e como pode rodar a aplicação?
* **Assertividade**: A aplicação está fazendo o que é esperado? Se tem algo faltando, o README explica o porquê?
* **Legibilidade do código** (incluindo comentários)
* **Segurança**: Existe alguma vulnerabilidade clara?
* **Cobertura de testes** (Não esperamos cobertura completa mas é importante garantir o fluxo principal)
* **Histórico de commits** (estrutura e qualidade)
* **UX**: A API é intuitiva?
* **Escolhas técnicas**: A escolha das bibliotecas, banco de dados, arquitetura, etc, é a melhor escolha para a aplicação?

## Dúvidas

Quaisquer dúvidas que você venha a ter, consulte as issues para ver se alguém já não a fez e caso você não ache sua resposta, abra você mesmo uma nova issue!

Ao completar o desafio, submeta um pull-request a esse repositório com uma breve explicação das decisões tomadas e principalmente as instruções para execução do projeto.

**Boa sorte! ;)**


## Requisitos

* O projeto precisa estar configurado para rodar em um ambiente macOS ou Ubuntu (preferencialmente como container Docker).
* Deve anexar ao seu projeto uma coleção do postman com todos os endpoints criados e exemplos de utilização.

**Para executar seu código devemos executar apenas os seguintes comandos**:

* git clone $seu-fork
* cd $seu-fork
* comando para instalar dependências
* comando para executar a aplicação

## Critério de avaliação

* **Organização do código**: Separação de módulos, view e model
* **Clareza**: O README explica de forma resumida qual é o problema e como pode rodar a aplicação?
* **Assertividade**: A aplicação está fazendo o que é esperado? Se tem algo faltando, o README explica o porquê?
* **Legibilidade do código** (incluindo comentários)
* **Segurança**: Existe alguma vulnerabilidade clara?
* **Cobertura de testes** (Não esperamos cobertura completa mas é importante garantir o fluxo principal)
* **Histórico de commits** (estrutura e qualidade)
* **UX**: A API é intuitiva?
* **Escolhas técnicas**: A escolha das bibliotecas, banco de dados, arquitetura, etc, é a melhor escolha para a aplicação?

## Dúvidas

Quaisquer dúvidas que você venha a ter, consulte as issues para ver se alguém já não a fez e caso você não ache sua resposta, abra você mesmo uma nova issue!

Ao completar o desafio, submeta um pull-request a esse repositório com uma breve explicação das decisões tomadas e principalmente as instruções para execução do projeto.

**Boa sorte! ;)**
## Execução do Projeto

```bash
$ git clone ...
$ docker-compose build
$ docker-compose up
# Acesse http://0.0.0.0:8000/admin/
# username: admin
# password: admin
```
## Diagrama das Pastas e Arquivos do Projeto
  A aplicação app é dividida em dois APPs: accounts e quiz.

  - desafio-backend
    - app
      - accounts
        - tests
          - test_accounts_model.py
          - test_accounts_api.py
        - __init__.py
        - admin.py
        - api.py
        - apps.py
        - forms.py
        - managers.py
        - models.py
        - serializers.py
        - urls.py   
      - quiz
        - tests
          - test_quiz_models.py
          - test_quiz_api.py
        - __init__.py
        - admin.py
        - api.py
        - apps.py
        - models.py
        - serializers.py
        - urls.py        
       - QuizzBizz
        - __init__.py
        - settings.py
        - urls.py
        - wsgi.py
      - db.sqlite3
      - docker-compose.yml
      - Dockerfile
      - manage.py
      - LICENSE
      - README.md 
      - requirements.txt



* **DB sqlite3**

- OBS: Foi escolhido o banco de dados SQLite3, pois os mesmo é relacional e leve, sem necessidade de configuração para utilizá-lo.
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


### Como Administrador
* Adicionar/Atualizar/Deletar questionários e todos os outros cadastros oriundos de ações do player.

### Como Player
* Registrar ou logar com nome de usuário e senha.
* Listar todos os questinários cadastrados.
* Visualizar perguntas e opções de respostas para um determinado questionário.
* Enviar resposta para uma determinada questão de um respectivo questionário.
* Listar o seu desempenho para todos os questionários respondidos.
* Visualizar ranking geral por quiz.
* Visualizar ranking por categoria.

## Endpoints
* Player Register
  - Descrição: Endpoint para criação de um novo player.
  - Método: POST
  - URL: http://0.0.0.0:8000/accounts/auth/register/
  - Body:
    - Format: json
    - { "name:" "", "username" : " ", "email": " ", "password": " ", }

* Player Login
  - Descrição: Endpoint para login de um respectivo player.
  - Método: POST
  - URL: http://0.0.0.0:8000/accounts/auth/login/
  - Body:
    - Format: json
    - { "username" : " ", "password": " "}  

* List Quizzes
  - Descrição: Endpoint para visualizar todos os questionários cadastrados no sistema.
  - Método: GET
  - URL: http://0.0.0.0:8000/api/quizzes/
  - Headers:
    - Authorization: Token *Insira o token*

* View Questions
  - Descrição: Endpoint para visualizar as questões de um quastionário específico
  - Método: GET
  - URL: http://0.0.0.0:8000/api/quizzes/${slug-quiz}$/
  - Headers:
    - Authorization: Token *Insira o token*

* Submit Answers
  - Descrição: Endpoint para envio da resposta escolhida pelo player para uma determinada questão de um quiz.
  - Método: POST
  - URL: http://0.0.0.0:8000/api/quizzes/${slug-quiz}$/submit/
  - Body:
    - Format: json
    - {"quiztaker": "", "question" : "", "answer": " "}
    - OBS: question e answer devem ser os ids da questão a ser respondida e a resposta escolhida pelo usuário, respectivamente, quiz_taker é respectivo ao "id", quiztaker_set.
  - Headers:
    - Authorization: Token *Insira o token*

* My Results
  - Descrição: Endpoint onde o usuário visualiza todos os questionários onde participou
  - Método: GET
  - URL: http://0.0.0.0:8000/api/my-quizzes/
  - Headers:
    - Authorization: Token *Insira o token*

* Ranking by Quiz
  - Descrição: Endpoint onde o usuário visualiza o ranking geral dos questionários respondidos.
  - Método: GET
  - URL: http://0.0.0.0:8000/api/ranking/${slug-quiz}$/
  - Headers:
    - Authorization: Token *Insira o token*



* OBS: Todos os endpoints podem ser acessados através do postman. 

## Testes

- Os testes implementados podem ser acessados na pasta "Tests" de cada aplicativo, ou seja, existe uma pasta "Tests" para o APP "quiz" e uma para o APP "accounts".
Foram testados os models e as conexões com os endpoints.


Para executar os testes:
```
bash

$ docker-compose run app pytest
```

## Dificuldades Encontradas

- Durante a realização do projeto tive dificuldades em entender o sistema de testes, sendo assim não sei se o que foi implementando está condizente com a necessidade do projeto, não tendo encontrado informação para realizar os testes de uma forma mais eficiente.

