## <img src="https://valora.cc/img/logo2.png" alt="Valora" width="24" /> Desafio Backend Python

Esse projeto é uma API de uma aplicação para a criação de um quiz de perguntas e respostas, as seguintes ferramentas foram utilizadas
* Python 
* Django 
* Django REST Framework
* Docker 


## Pontos já desenvolvidos:

* **CRUD para as perguntas e respostas**
* **Categorias associadas a cada novo quiz**
* **Abstração de banco de dados**
* **Autenticação via token**
* **Paginação**
* **Separação clara dos módulos**
* **Configurações docker**
* **CRUD de usuários porem por hora só pela ferramenta de admin que pode ser acessada pelo seguinte link:**
    ```
    http://127.0.0.1:8000/admin/
    ```
    Essa ferramenta pode ser acessa pelo seguinte usuario de teste

    ```
    login: guilherme
    senha: 123456
    ```

## Pontos em desenvolvimento:

* **Rank**:

    O Rank possui somente modelo e sua abstração de banco dados, estou tento dificuldade na integração do seu modelo com os demais para a aplicação do somatório da sua pontuação 
* **Testes**:
    
    Os teste ainda não foram iniciados


## Iniciando o projeto:

Antes de iniciar remendo fortemente que ative o ambiente virtual, não é obrigatório, mas ajuda a evitar conflito de versão

No Windows isso é possível com o seguinte comando:
```
venv\Scripts\activate.bat
```

Em seguida as libs usadas com o comando:
```
pip install -r requirements.txt
``` 

E por último inicie a api com o comando:
```
python manage.py runserver
```
