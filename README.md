# Valora quiz ![valora logo][i01]

[![l13]][l14]
[![l09]][l10]
[![l11]][l12]
[![l15]][l16]

Quiz defafio para backend Python/Django.

[Requisitos originais][r01].

## Características

Projeto iniciado utilizando [Django Cookiecutter][l01] como recomendado nos livros dos Greenfelds [Two Scoops of Django][l02] e [Django Crash Course][l03] como bootstrap para projetos utilizando Django.

Testes unitários com [Pytest][l04] e com mocks de teste utilizando o [Factory Boy][l05].

Qualidade de código checada com [Flake8][l06], assegurando conformidade com a [PEP-8][l07] e outras PEPs e plugins que asseguram boas práticas em tratamentos de excessẽs, docstrings, comprehensions, comentários, etc.

Implemetação simples de um publish/subscriber como alternativa ao uso de Django signals, uma vez que são considerados como recurso a ser evitado.

Código consiso, poucas linhas de código por funções, buscando aprooveitar as funcionalidades dos frameworks e libs utilizadas.

Commits atomicos, seguindo com mensagens seguindo o padrão [Conventional Commits][l08].

Utilização do formatador de códigos Python YAPF no padrão Google.

Uso de pre commits hooks, assegurando a qualidade de código a cada commit.

## Execução

O projeto foi desenvolvido e testado em sistema operacional Linux Ubuntu, portanto não há garantia do seu funcionamento em Windows, Mac ou distro Linux não baseada em Debian.

1. Clonar o repositório

```shell
git clone https://github.com/diego-marcelino/valora-quiz.git
```

2. Construir a imagem

```shell
make build
```

3. Exceutar o projeto

```shell
make run
```

Há um conjunto de dados disponível. Para carregá-lo no banco de dados utilizar o comando

```shell
make loaddata
```

## Acesso

Após executar a inicialização do projeto, estará disponível em _localhost:8000_. Uma interface com Swagger estará acessível para consultar os endpoints e realizar requisições.

Para utilizar autenticação no Swagger:

1. Fazer login atraves do endpoint de login e copiar o token de acesso.

2. Clicar no botão _Authorize_

![Botão Authorize][i03]

3. Digitar: _Bearer_ + o token de acesso

  ![Bearer token com Swagger][i02]

4. Todas as requisições serão feitas com o token de acesso informado.

Para fazer logout e utilizar outras credenciais clicar novamente no botão _Authorize_ e _Logout_, então repetir o processo para as novas credenciais.

![Logout do Swagger][i04]

### PgAdmin

Há uma imagem do pgAdmin para acessar o banco de dados Postgres do projeto, disponível em _http://localhost:9000_.

Para login na interface do pgAdmin utilizar as credenciais: username: _admin@admin.com_ password: _admin_.

Para adicionar a conexão com o banco de dados utilizar a configuração seguinte com password: _dbpassword_.

![Conexão pAdmin][i07]

## Utilização

### Admin

1. Cria usuário atraves da rota signup e utiliza 'A' no atributo 'role'

2. Faz login com suas credenciais pela rota 'login' e obtem seu json web token de acesso.

3. Faz cadastro de categorias. Permissão de escrita e leitura.

4. Faz cadastro de questões. Permissão de escrita e leitura.

### Player

1. Cria usuário atraves da rota signup e utiliza 'P' no atributo 'role'

2. Faz login com suas credenciais pela rota 'login' e obtem seu json web token de acesso.

3. Consulta as categorias disponíveis. Permissão somente de leitura.

4. Cria um novo quiz informando a categoria desejada. Pode consultar seu quiz em aberto.

5. Envia as respostas para o quiz em aberto, informando o id da questão e o indice da sua escolha.

6. Consulta o ranking geral e por categoria a qualquer momento após logado.

## Testes

Os testes unitários foram desenvolvidos com [Pytest][l04] e mocks de teste utilizando o [Factory Boy][l05].

Para executar os testes unitários utilizar o comando:

```shell
make tests
```

![Unit tests][i05]

Para obter o report do coverage:

```shell
make report
```

![Coverage Report][i06]

## Integração contínua

A integração contínua (CI) é feita pelo Github Actions.

O pipeline consiste em verificar a qualidade do código com o Flake8 e executar os testes unitários.

---

## <span style="color:green">Find the easter egg!</span>

---

<!-- Links -->
[l01]: https://cookiecutter-django.readthedocs.io/en/latest/ "Django Cookiecutter"
[l02]: https://b-ok.lat/book/2951511/0e8113 "Two Scoops of Django"
[l03]: https://b-ok.lat/book/5412804/9c7fd0 "Django Crash Course"
[l04]: https://docs.pytest.org "Pytes"
[l05]: https://factoryboy.readthedocs.io "Factory Boy"
[l06]: https://flake8.pycqa.org "Flake8"
[l07]: https://www.python.org/dev/peps/pep-0008/ "PEP-8"
[l08]: https://www.conventionalcommits.org/en/v1.0.0/ "Conventional Commits"
[l09]: https://img.shields.io/badge/code%20style-YAPF-000000.svg "YAPF Badge"
[l10]: https://github.com/google/yapf "YAPF Repo"
[l11]: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg "Django Cookiecutter Badge"
[l12]: https://github.com/pydanny/cookiecutter-django/ "Django Cookiecutter Repo"
[l13]: https://github.com/diego-marcelino/valora-quiz/workflows/CI/badge.svg "Github Badge"
[l14]: https://github.com/diego-marcelino/valora-quiz/actions "Github Actions"
[l15]: https://img.shields.io/badge/-Diego%20Marcelino-blue?logo=Linkedin&logoColor=white "Linkedin Badge"
[l16]: https://www.linkedin.com/in/diegomarcelino/ "Linkedin Diego Marcelino"
<!-- References -->
[r01]: requirements.md "requisitos originais"
<!-- Imagens -->
[i01]: https://valora.cc/img/logo2.png "Valora logo"
[i02]: images/swagger_bearer.png "Bearer token com Swagger"
[i03]: images/swagger_authorize.png "Botão Authorize"
[i04]: images/swagger_logout.png "Swagger Logout"
[i05]: images/unit-tests.png "Unit tests"
[i06]: images/coverage-report.png "Coverage report"
[i07]: images/pgadmin.png "pg Admin server"
