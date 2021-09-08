# **Valora**
## **Como executar a aplicação**
### **Requisitos**

* Docker
* 

> **_NOTE:_**  Podem haver outros requisitos não detectados, como gcc, g++, mysqlclient.

---
### **Configurações**

Primeiro de tudo, altere o arquivo `.env` da forma como desejar. O indicado é que apenas se alterem as portas que serão abertas, de forma que não haja conflito com outras aplicações.

---
### **Execução**

> **_NOTE:_**  A primeira execução pode levar alguns minutos para preparar as aplicações, devido à ter que fazer download das imagens docker e criação de novos containers.

Para executar o projeto, basta utilizar o comando `docker-compose up`.
o comando fará os seguintes procedimentos:

* Criará dois bancos de dados, sendo um para o projeto e outro para testes;
* Conectará o banco de dados do projeto ao PHPMyadmin;
* Criará um container django a partir do Dockerfile especificado;
* Executará o entrypoint especificado no docker-compose.yml:
  * O entrypoint fará a coleta de arquivos estáticos;
  * Criará novas migrations;
  * Aplicará as migrations ao banco de dados;
  * Fará testes unitários se a variável `DEBUG` estiver definida com `True` no `.env`;
  * Iniciará o servidor web;


Para acessar a aplicação no navegador, basta acessar o HOST especificado no arquivo `.env`, seguido da porta de cada container. Ex:

192.168.0.175:8000

---

### **Testes**

Para executar os testes unitários de acordo com as configurações do arquivo `pytest.ini`, basta utilizar o comando `pytest`.

> **_NOTE:_**  Necessário acessar o shell do container do django.

---

### **Debug**

Se a variável `DEBUG` estiver definida como `True` no `.env`, a aplicação irá rodar em modo debug, e o desenvolvedor terá acesso ao menu do pacote debug_toolbar na aplicação.

---

### **API**

Todos os endpoints da aplicação estão disponíveis na rota `api/`.

---

## **Estruturação da aplicação**
### **asdf**

## **Pontos a Melhorar**

* Permissões
* Senha de usuário através do admin (Porque o django faz encryptação da senha)
* Separar ranking de criar novo usuário