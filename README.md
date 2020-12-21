# Desafio Backend Python

### Techs

* [Django] - Python Web library 
* [Django Rest Framework] - Python Web Library for API`s 
* [SQLite 3] - Simple database for prototipes

All the code is open source with a public repository on GitHub.

### Clone project

```sh
$ git clone https://github.com/luigus/desafio-backend desafio-backend-luigus 
$ cd desafio-backend-luigus/valora
$ git checkout develop
```
### Create Docker Image
```sh
$ docker build -t django-image -f Dockerfile .
```
### Run Docker Container
```sh
$ docker run -it -p 8000:8000 django-image
```

### API
 File with all API calls : Valora.postman_collection.json

| API | METHOD | ENDPOINTS | USER | 
| ------ | ------ |------ |------ |
| List of categories | GET | /api/category/ | Player/Admin | 
| Category description | GET |/api/category/<id_category>/ | Player/Admin | 
| New Category | POST |/api/category/ | Admin | 
| List of questions | GET | /api/question/ | Player/Admin | 
| Question description | GET |/api/question/<id_question>/ | Player/Admin | 
| List of questions by category| GET | /api/question/category/<id_category>/ | Player/Admin | 
| New Question | POST |/api/question/ | Admin | 
| List of answers of all users | GET | /api/answer/ | Player/Admin | 
| List of answers by user | GET |/api/answer/author/<id_author>/ | Player/Admin | 
| New Answer | POST |/api/question/ | Player/Admin | 
| List of ranking of all categories | GET |/api/ranking/ | Player/Admin | 
| List of ranking by categories | GET |/api/ranking/category/<id_category>/ | Player/Admin | 


### Django super-user

* User: luigus
* Password: MOMOeang

### Django tests
For run models and views tests use this comand below :
```sh
$ python manage.py test quiz
```

### Todos
 - Develop the front-end
 - Check security of the API

License
----

MIT

   
   
