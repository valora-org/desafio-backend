# Introdução

Este é o repositório de uma API para quiz, onde pode criar perguntas, consultar ranking e responder quiz. Cada quiz contém 10 perguntas e para cada pergunta, contém 3 alternativas, sendo que apenas uma é correta.

# Requisito

* Executar .sh
* Docker
* Docker Compose

# O que foi usado

* PostgreSQL
* Python
* Django
* Django REST Framework
* Docker
* Docker Compose
* Test do Django REST Framework

# Como funciona

Para iniciar pela primeira vez a API existe um arquivo de extensão `.sh`  que irá fazer a build usando o Docker Compose, subir os Containers (o container `db` irá executar um backup do banco para popular o banco), esperar 1 min (tempo necessário para popular o banco) e descer os containers. Após isso, é só executar o compose. Comandos abaixo:

```
./instalar.sh
docker-compose up
```

###### Observação

Pode ser necessário dar permissão para o arquivo `instalar.sh`

Para isso execute o comando abaixo:

```
chmod +x instalar.sh
```

##### Fluxo para jogar

1. Inicie o quiz pela url `http://0.0.0.0:8000/` com o método `POST` enviando a categoria como o exemplo abaixo:

   ```
   {
       "categoria": "esporte"
   }
   ```
2. Faça um `GET` na url `http://0.0.0.0:8000/play/` para obter a pergunta. Abaixo um exemplo de pergunta que será retornada:

   ```
   {
       "Pergunta": "Em que país pertence a Liga Calcio?",
       "a": "Alemanha",
       "b": "Itália",
       "c": "Espanha"
   }
   ```
3. Envie a resposta via POST para a url http://0.0.0.0:8000/resposta/ com o texto da alternativa como o exemplo abaixo:

   ```
   {
       "resposta": "Itália"
   }
   ```
4. Consulte as perguntas até responder todas as 10.

##### Fluxo para criar pergunta

Faça um `POST` na url `http://0.0.0.0:8000/perguntas/` como o exemplo abaixo:

```
{
	"pergunta": "Qual foram os Brasileios eleitos Melhores do Mundo?",
	"categoria": "esporte",
	"alternativa_correta": "Friesdenrei ,Agostinho Fortes,Domingos da Guia,Pelé,Ronaldo,Rivaldo,Adriano e Robinho",
	"alternativa1": "Ronaldo,Rivaldo,Adriano e Robinho",
	"alternativa2": "Pelé,Ronaldo,Rivaldo,Adriano e Robinho"
}
```

##### Fluxo para consultar ranking

Existe dois tipos de consulta do ranking:

* Ranking geral
  * Faça um `GET` na url `http://0.0.0.0:8000/ranking/`
* Ranking por categoria
  * Faça um `POST` na url `http://0.0.0.0:8000/ranking/` informando a categoria como o exemplo abaixo:

    ```
    {
        "categoria": "esporte"
    }
    ```

# Teste

Para realizar os teste, foi utilizado o test do Django REST Framework. Para sua execução basta usar o comando abaixo:

```
./manage.py test
```

# Backup

O backup que será usado para popular o banco contém:

##### User

| Username | Senha          | Função                                                                         |
| -------- | -------------- | -------------------------------------------------------------------------------- |
| root     | naotemsenha123 | Acesso ao admin do Django                                                        |
| alice    | naotemsenha123 | **Admin** - Tem permissão para criar perguntas e respostas para os quizes |
| raphael  | naotemsenha123 | **Player** - Tem permissão para jogar e consultar o ranking               |

##### Categoria

Uma categoria que é `esporte`

##### Pergunta

12 perguntas pertencentes a única categoria na base esporte

##### Resposta

36 respostas, sendo que cada 3 respostas pertence a uma pergunta

# Endpoints

Todos os endpoints estão com a autenticação por `Session`, `Basic` (usuário e senha) e `Token`

|            EndPoint            |    Método    | Usuário |                   Função                   |                                      Parâmetro                                      |         Retorna         |
| :----------------------------: | :-----------: | :------: | :-------------------------------------------: | :----------------------------------------------------------------------------------: | :---------------------: |
|      http://0.0.0.0:8000/      |     POST     |  player  |             Inicia criando o quiz             |                                      categoria                                      |        Perguntas        |
|   http://0.0.0.0:8000/play/   |      GET      |  player  |                Busca pergunta                |                                     ------------                                     | Pergunta e alternativas |
| http://0.0.0.0:8000/resposta/ |     POST     |  player  | Responder pergunta<br />com texto da resposta |                                       resposta                                       |     Certo ou Errado     |
| http://0.0.0.0:8000/perguntas/ |     POST     |  admin  |                Criar pergunta                | pergunta<br />categoria<br />alternativa_correta<br />alternativa1<br />alternativa2 |         detail         |
|  http://0.0.0.0:8000/ranking/  | POST<br />GET |  player  |                  Ver ranking                  |                                   categoria (POST)                                   |         Ranking         |

# Considerações finais

Na modelagem eu pensei em uma API um pouco mais simples, sem salvar a resposta no banco, pois não vi necessidade, com isso, fiz um controle para saber em qual é a pergunta que ainda não foi respondida e evitar repetição, isso ajuda o quiz poder ser respondido por várias pessoas ao mesmo tempo, sem conflito entre os usuários e cada um respondendo o seu quiz.
