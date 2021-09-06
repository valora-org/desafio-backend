# API Quiz

* A ideia da API é fornecer um backend para uma aplicação de quiz por categoria
e ranking global ou categorizado.

* O usuários podem se registrar na API como players ou usuários administrativos.

- Usuários adminitrativos podem fazer edição de perguntas e respostas. Além,
de poderem joagar o quiz.

- Usuários players podem jogar o quiz.

* Ao selecionar uma categoria para o quiz, a API seleciona 10 perguntas e respostas
no banco de dados de forma aleatória e devolve para o usuário. Porém, caso a 
categoria não tenha perguntas suficientes para completar as 10, a API retorna um
erro, pois não há perguntas suficientes para o quiz.

* Ao finalizar o quiz o jogador receberá sua colocação no ranking global.

* O jogador poderá fazer a consulta do ranking global e também do ranking por
categoria, bastanto passar como parametro o id da categoria.

* O banco utilizado no momento é o sqlite. Essa escolha foi somente por comodide,
tendo em vista que o projeto será levantando com o docker-compose e seria necessário,
criar um container para outros bancos que poderiam ser utilizados. Porém, isso
não agregaria em nada na finalidade da API. Isso porque é somente um teste.
Logicamente, em um ambiente de homologação e produção eu usuaria ao menos um postgres.

* As perguntas cadastradas poderão ter várias respostas certas e erradas. A API
irá selecionar apenas uma alternativa correta e duas incorretas. Tudo randomicamente

## Para rodar o projeto

* Crie um arquivo .env na raiz do projeto e defina as variaveis de ambiente:
 - DEBUG
 - SECRET_KEY

 * Mesmo que vazio, crie o arquivo .env

 * Caso não seja definido as variaveis as mesmas pegará o valor default definidos
 direto no arquivo settings.py

 * Para executar o projeto tenha o docker e o docker-compose instalado na máquina
 
 * Rode o seguinte comando na raiz do projeto:
 - docker-compose up --build -d
 - O parametro -d serve para desocupar o terminal. Caso queira ver os logs, retire-o.

* Note que será criado dois containers docker. Um contendo o projeto python rodando
com gunicorn e outro com nginx que fará o repasse das chamadas e a entrega dos arquivos estáticos.

* O projeto rodará na porta 8007 de seu computador
- http://127.0.0.1:8007

* O arquivo "popule.dumb.sql" fará a população dos dados

## Usuários teste
Admin
username: admin
password: administrador

Player
username: bruno
password: bruno@12345

## Melhorias a fazer

- [] Definir um banco Postgres
- [] Paginação dos rankings
- [] Criar um docker-compose para cada ambiente (development, homologação e produção)
- [] Fazer o frontend para consumir a API
