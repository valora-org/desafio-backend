# API de uma aplicação para a criação de um quiz de perguntas e respostas.

Devido hoje ser o prazo limite de entrega do desafio, não vou conseguir entregar todos os requisitos.
Itens faltantes: pontuação, coleção do postman, ranking, docker, UI.
Independente do resultado do processo seletivo, vou continuar aprimorando o projeto do quiz.
Eu tinha começado a fazer a parte do docker e postgres como banco de dados, porém tive alguns probleminhas ao testar em outro ambiente e preferi remover as alterações, pois assim consigo exibir oque já consegui fazer do quiz.
Entendo que o SQLite não é um banco de dados de escolha para website profissionais e que Django tem suporte built-in para os bancos profissionais: PostgreSQL, MySQL e Oracle.

Com mais tempo eu melhoraria o visual do quiz, que foi algo que só consegui ter tempo de criar um basicão.
Achei que a ideia do desafio foi bem bacana, mas eu precisaria de mais tempo para poder concluí-la 100%, visto que tive que conciliar o desafio com as minhas outras atividades.


Para poder utilizar este repositório, utilizar:
```
git clone https://github.com/carolstoffel/valora.git
```

```
pip install requirements.txt
python manage.py runserver
```

Para inserir dados na API, só é aceito usuário administrador, portanto necessário logar com os dados em:
http://127.0.0.1:8000/admin
```
usuario: admin
senha: admin
```


Endpoints:

http://127.0.0.1:8000/api/v1/classificacao/

http://127.0.0.1:8000/api/v1/perguntas/
