<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/iamkamui/desafio-backend">
    <img src="/templates/static/assets/img/valoralogo.svg" alt="Logo" height="80">
  </a>

<h3 align="center">Valora Desafio Backend</h3>

  <p align="center">
    project_description
    <br />
    <a href="https://github.com/iamkamui/desafio-backend"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## Sobre o Projeto
API Root
![Desafio Backend][product-screenshot]

Visualização dos Quiz's
![Quiz List][product-quiz-list]

Respostas do Quiz '1'
![Quiz Answers][product-quiz-answers]

Lista de todas as respostas
![Answers List][product-answer-list]

Ranking geral
![Ranking][product-ranking-list]


API de uma aplicação para a criação de um quiz de perguntas e respostas, onde que a api disponibiliza a visualização de questões, usuários, ranking baseado em pontuação.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Desenvolvido com

* [![DRF][Django REST framework]][DRF-url]
* [![Python][Python.py]][Python-url]
* [![Django][Django]][Django-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Começando

Para visualizar este projeto você precisa de uma cópia local do mesmo e certificar que possui Docker/Pyhon/Git instalado:

### Pre requisitos

Certifique-se de editar o `.env_example` antes de prosseguir.

### Instalação

1. Faça um clone do repositório
   ```sh
   git clone https://github.com/iamkamui/desafio-backend.git
   ```
2. Crie a imagem docker
   ```sh
   docker-compose up
   ```
3. Faça a migração do banco de dados:

   ```sh
   docker-compose exec web python manage.py migrate
   ```
4. Acesse a API root
   ```sh
   127.0.0.1:8000/api/
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Uso

Para vizualizar o funcionamento da API, crie um super usuário através do comando:

```sh
docker-compose exec web python manage.py createsuperuser
```

Acesse o painel de login administrador:

```
127.0.0.1:8000/admin/
```

links API:

```
127.0.0.1:8000/api/quizzes/{pk} #Retorna uma questão especifica registrada dentro do quiz com as respostas
```
```
127.0.0.1:8000/api/quizzes/ #Retorna a lista de todos os quiz's existentes
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Testes

Os testes unitários foram desenvolvidos pelo APITestCase do Rest Framework.
para executar os testes utilizar o comando:

```sh

docker-compose exec web python manage.py test

```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Pedro Augusto - [Pedro Augusto](https://www.linkedin.com/in/pedro-augusto-b445b019b/)

Project Link: [https://github.com/iamkamui/desafio-backend](https://github.com/iamkamui/desafio-backend)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- IMPROVEMENTS -->
## Improvement points

* Arrumar número maximo de objetos, fazer identificar quando um(a) quiz/questão especifico(a) atinge o número máximo de questões/respostas
* Ranking por categoria de quiz

## Bugs

* função número maximo, atingindo todos objetos e não filtrando por id


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/pedro-augusto-b445b019b/

[product-screenshot]: /templates/static/assets/img/apiroot.png

[product-quiz-answers]: /templates/static/assets/img/quizanswers.png

[product-quiz-list]: /templates/static/assets/img/quizlist.png

[product-ranking-list]: /templates/static/assets/img/rankinglist.png

[product-answer-list]: /templates/static/assets/img/answerlist.png

[Django REST framework]: https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray
[DRF-url]: https://www.django-rest-framework.org/

[Python.py]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=white&color=4FC08D&labelColor=gray
[Python-url]: https://www.python.org/

[Django]: https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white&labelColor=gray
[Django-url]: https://www.djangoproject.com/
