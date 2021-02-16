# Quiz

## Desenvolvimento
### Usando pipenv
 - Instale a ferramenta Pipenv, https://pipenv.pypa.io/en/latest/install/#installing-pipenv
 - Instale as dependências do projeto com: ```pipenv install```
### Usando virtualenv
 - Crie seu virtualenv, ative e instale as dependências: ```pip install -r requirements.txt```

## Configuração
 - Crie um arquivo ```.env```, baseado no exemplo em ```.env.example```
### Banco de dados:
 - O projeto já suporta o banco sqlite, para utilizar outros bancos, instale o conector equivalente e configure a url em ```.env```
 - Exemplos de padrão de url para vários bancos podem ser encontrados em: https://github.com/jacobian/dj-database-url#url-schema

## Rodando
### Migrando o banco
```bash
pipenv run python manage.py migrate
```
### Criando um usuário administrador
```bash
pipenv run python manage.py createsuperuser
```
### Iniciando o servidor com docker:
```bash
docker-compose up
```
### Iniciando o servidor usando o pipenv
```bash
pipenv run python manage.py collectstatic
pipenv run python manage.py runserver
```
## Documentação
 - A documentação da API pode ser vista acessando a url em: ```/docs/```
