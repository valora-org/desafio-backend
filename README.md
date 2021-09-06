
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
| Calcule results and list user's point and ranking | GET | TO DO | player/admin | 
