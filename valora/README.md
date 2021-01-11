## <img src="https://valora.cc/img/logo2.png" alt="Valora" width="24" /> Desafio Backend Python

## 


[![CI](https://github.com/AlbertoWagner/desafio-backend/workflows/CI/badge.svg?event=push)](https://github.com/AlbertoWagner/desafio-backend/actions)
[![license](https://img.shields.io/github/license/AlbertoWagner/desafio-backend.svg)](https://github.com/AlbertoWagner/desafio-backend/blob/master/valora/LICENSE)


##Tech Stack:


* **Python**
* **Django**
* **Django REST Framework**
* **Pytest**
* **Docker**

## Desenvolvimento

Para iniciar o desenvolvimento, é necessário clonar o projeto do GitHub num diretório da sua preferência:

```shell
cd "diretorio de sua preferencia"
git clone https://github.com/AlbertoWagner/desafio-backend.git
cd desafio-backend
git checkout master
cd valora
sudo docker-compose up --build -d
"O projeto estará disponível em https://127.0.0.1:8000."
"Para da o stop no projeto o comando é"
sudo docker-compose stop

```

## Django super-user
```shell
User: admin
Password: admin123
```

## Testes

Para rodar os testes, utilize o comando abaixo:

```
./manage.py test quiz.tests.quiz_test
./manage.py test user.tests.user_test
./manage.py test user.tests.user_permissions
```



# Para roda o script no python console para alimenta o banco de questões.


```shell
 script :
 from quiz import scrip_add_question
 alimentar_banco()

```

### Autor
---

<a href="#">
 <sub><b>Alberto Wagner</b></sub></a> <a href="#" ></a>


Feito por Alberto 👋🏽 Entre em contato!

[![Linkedin Badge](https://img.shields.io/badge/-Alberto-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/alberto-wagner-5571a3106/)](https://www.linkedin.com/in/alberto-wagner-5571a3106/) 
[![Gmail Badge](https://img.shields.io/badge/-albertow475@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:albertow475@gmail.com)](mailto:albertow475@gmail.com
)