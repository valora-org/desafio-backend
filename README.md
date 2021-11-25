# Teste Para desenvolvedor - Valora

Desenvolvedor Ricardo Enehias

# Resumo

- Projeto de API desenvolvido com django rest framework, autenticação por Token, rodando em um SGBD MySql,
  conteinerização com docker.

# Requisitos

- docker-compose versão 1.29 ou compatível
- docker-compose versão 20.10 ou compatível

# Instalação

Clonar o projeto

````
git clone https://github.com/enehias/desafio-backend.git
````

Acessar pasta do projeto

````
cd desafio-backend
````

Iniciar build, e deploy do contêiner

````
make iniciar-app 
````

Rodar dados para aplicação

````
make init-data-app 
````
-Aplicação irá rodar http://127.0.0.1:8000
# Regras de negoócio
- o usuário tipo admin, tem autorização completa no sistema
- o usuario player pode apenas, iniciar um jogo, finalizar e consulta  seus jogos, e consultar rankings
- usuário tipo admin, tem o atributo is_staff como verdadeiro, enquanto os players falso

- Usuários Iniciais
    - Admin
        - username: adminValora
        - password: 1234
        - is_staff: true
    - Player
        - username: playerValora
        - password: 1234
        - is_staff: false
        
# Principais Endpoints

Todas as rotas são protegidas com Token(exceto login)

| Descrição                                   | URI              | Método | Payload                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------- | ---------------- | ------ | ---------- |
| Logar na aplicação                          | login/        | POST      | ```{"username": "adminValora", "password":"1234"}```   |                                                                                                                                                                                                                                                                                                             |
| Criar uma categoria                          | categoria/     | POST   |  ```{"nome":"Tecnologia"}``` |
| Listar todas as categoria na base de dados | categoria/      | GET    | Não se aplica       |      
| Criar questão             | questao/ | POST    | ```{"texto":"Pergunta X?","categoria":1}```|                                                                                                                                                                                                                                                                                             |
| Pesquisar uma questão                            | questao/{id}        | GET   | params: - id: id da questão   |
| Listar todas as questões na base de dados | questao/      | GET    | Não se aplica       |                                                                                                                                                                                                                                                                                                                    |
| Criar resposta             | questao/ | POST    | ```{"texto":"Resposta X!","questão":1,correta:true}```|                                                                                                                                                                                                                                                                                             |
| Pesquisar uma resposta                            | resposta/{id}        | GET   | params: - id: id da resposta   |
| Listar todas as respostas na base de dados | resposta/      | GET    | Não se aplica       | 
| Iniciar Quiz | iniciar-jogo/      | POST    | ```{"categoria":2}```       | 
| Pesquisar Quiz | buscar-jogo/{id}      | GET    | params: - id: id do jogo|
| Finalizar Quiz | finalizar-jogo/{id}      | PUT    | ```{"respostas":[{"questao":1,"resposta":3},{"questao":2,"resposta":6},{"questao":3,"resposta":9}]```<br>params: - id: id do jogo|
| Ranking Global | ranking/global      | GET    | Não se aplica|
| Ranking Categoria | ranking/categoria      | GET    | Não se aplica|