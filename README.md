
# quiz
## Dependences

```bash
sudo apt-get install -y \
python3-setuptools \
python3-pip \
python3-dev \
python3-venv \
git

```

## Dev 
```bash
# Clones repository
git clone https://github.com/dssantos/desafio-backend quiz
cd quiz
# Creates venv
python3 -m venv .quiz
source .quiz/bin/activate
# Install libraries
python -m pip install -U pip
pip install -r requirements.txt
# Environment variables
cp quiz/contrib/.env-sample .env
SECRET_KEY=`python quiz/contrib/secret_gen.py`
sed -i "/^SECRET_KEY=/c\SECRET_KEY=${SECRET_KEY}" .env

```

## Tests
```bash
# Run tests
python manage.py test

```

## Run
```bash
# Run server
python manage.py runserver

```
## Access server
<http://127.0.0.1:8000/>

## Credentials

admin: 1

player: 1

## Endpoints
| API | METHOD | ENDPOINTS | USER | 
| ------ | ------ |------ |------ |
| List of categories | GET | /category/ | player/admin | 
| Category description | GET | /category/<id_category>/ | player/admin | 
| New Category | POST | category/ | admin | 
| List of questions | GET | /question/ | player/admin | 
| Question description | GET | /question/<id_question>/ | player/admin | 
| New Question | POST | question/ | admin | 
| List of categories avalaible to quiz | GET | /choosequiz/ | player/admin | 
| List of 10 questions and answers of selected category | GET | /startquiz/<id_category>/ | player/admin | 
| Calcule quiz results and list user's point and ranking | POST | /result/ | player/admin | 

## Postman collection
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/d2bd389aa67ec7f128ed)

## Examples using httpie in bash
```bash
# List of categories
http -a admin:1 http://127.0.0.1:8000/category/
# Category 1 description
http -a admin:1 http://127.0.0.1:8000/category/1/
# New category
echo '{"category":"C4"}' | http -a admin:1 POST http://127.0.0.1:8000/category/
# List of questions
http -a admin:1 http://127.0.0.1:8000/question/
# Question 1 description
http -a admin:1 http://127.0.0.1:8000/question/1/
# New question
echo '{"category": "http://127.0.0.1:8000/category/3/","question": "Q12","answer1": "A1","answer2": "A2","answer3": "A3","right_answer": "A3"}' | http -a admin:1 POST http://127.0.0.1:8000/question/
# List of categories avalaible to quiz
http -a player:1 http://127.0.0.1:8000/choosequiz/
# List of 10 questions and answers of category 1
http -a player:1 http://127.0.0.1:8000/startquiz/1/
# Calcule quiz results and list user's score and ranking
echo '{"category":"1", "answers": {"1":"A1", "2":"A1", "3":"A1", "4":"A2", "5":"A3", "6":"A1", "7":"A1", "8":"A1", "9":"A1", "10":"A1"}}' | http -a player:1 POST http://127.0.0.1:8000/result/
```