# Quiz Api
Desafio backend para um quiz desenvolvido em Python e Django.


## Especificação técnica
- O projeto foi desenvolvido usando Django rest framework para api, JWT para autenticação e
 geração de token, banco de dados PostgreSQL que rodará em um container Docker.

## Importante
- É pré-requisito ter o Docker instalado na maquina onde será 'deployado'.
- Para deploy do projeto será necessario ter o 'Make' para o uso de comandos makefile.
- Para instalar caso necessario: ```sudo apt-get install build-essential```

## Deploy
1. Abrir o prompt de comando ou bash.
2. Clonar o projeto: ``` git clone https://github.com/anthonylopez15/quiz.git ```
3. Ir até a pasta raiz do projeto: ```cd quiz```
4. Iniciar os serviços: ```make start-services```
5. Verificar se o servidor está rodando: http://localhost:8000/api/

# Regras de negócio
- Somente o usuário Admin pode criar perguntas e respostas.
- O usuário Player somente poderá jogar e consultar o ranking.
- O que define o tipo de usuário é o campo ``is_staff: true`` para admin, ``is_staff: false`` 
para usuario não admin. Por default o campo é false caso não seja passado no body da request.
- Por padrão, no deploy é criado um usuário super admin Django como mostra o exemplo na url ``/api/token/`` a seguir.


# Endpoints
## Fluxo do quiz
- Login:
```
POST - api/token/
{
    "username": "admin@gmail.com",
    "password": "Pass.123"
}
```
- Criar categoria:
```
POST /api/category/
{
    "description": "Musica"
}
```
- Criar perguntas:
```
POST /api/question/
{
    "category": 1,
    "question": [
        {
            "question": "Pergunta 1?",
            "answer": [
                {
                    "answer": "Resposta 1.1",
                    "is_right": false
                },
                ...
            ]
        },
         {
            "question": "Pergunta 2?",
            "answer": [
                {
                    "answer": "Resposta 1.2",
                    "is_right": false
                },
                ...
            ]
        },
        ...
    ]
}
```
- Pesquisar por category: 
```
GET /api/category?search={CATEGORY_DESCRIPTION}
```
- Começar um quiz por categoria:
```
POST /api/quiz/
{
    "user": 1,
    "category": 2
}
```
- Responder perguntas: 
```
PUT /api/quiz/{ID_QUIZ}/
{
    "question": 15,
    "answer": 44
}
```
- Finalizar quiz: 
```
POST /api/quiz/{ID_QUIZ}/finish/
```
- Ranking global 
```
GET /api/quiz/ranking-global/
```
- Ranking por categoria
```
GET /api/quiz/ranking-by-category/
```
- Criar usuario:
```
POST /api/user/
{
    "username": "player_1",
    "password": "Player.123",
    "email": "player.1@gmail.com",
    "name": "Player",
    "is_staff": false (not required)
}
```

## Caso de teste
- Na pasta raiz do projeto foi disponibilizado o arquivo de configuração de todos os 
endpoints na qual será necessário importá-lo para testar no postman.
- Será necessário adicionar o token nas variaveis de ambiente do postman para que seja passado no header da 
request para autenticação.
- Todas as urls se encontram no postman e podem ser testadas.
- Para rodar os testes unitários: ``make test``

### Comandos Make
1. Criar o build dos containers ``make build``
2. Iniciar os containers docker``make start``
3. Para os containers ``make stop``
4. Deletar os serviços ``make down``
5. Inciar todos os serviços de uma vez ``make start-services``
6. Inciar unit test ``make test``
7. Popular o banco com dados ficticios ``make build-data``
