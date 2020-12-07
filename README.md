! Required: Docker Compose or Docker Desktop for Mac/Windows

1 - Initial Setup:

  run:
  
    docker-compose up
  
  
2 - EM OUTRO TERMINAL
  
  run:
    
    docker container ls

3 - Copie o ID do container postgres
  
4 - Execute (Substitua abaixo 53e14a9597d5 pelo ID do container copiado no passo anterior):
    
    cat dump_2020-12-06_16_57_08.sql | docker exec -i 53e14a9597d5 psql -U postgres -d postgres
  


    

## <img src="https://valora.cc/img/logo2.png" alt="Valora" width="24" /> Desafio Backend Python

Parabéns! Se você chegou até aqui significa que você passou pelas etapas mais difíceis do nosso processo seletivo. Somos extremamente criteriosos com as pessoas que vão integrar nosso time porque só aceitamos pessoas incríveis!

Agora é a parte fácil. Chegou a hora de mostrar todas as suas habilidades de transformar café em código. Vamos lá?

Nesse desafio iremos avaliar suas habilidades em:

* **Python**
* **Django**
* **Django REST Framework**
* **Pytest**
* **Docker**

Você irá desenvolver a API de uma aplicação para a criação de um quiz de perguntas e respostas!

**A aplicação deverá prover o registro e autenticação de dois tipos de usuários**:

* Admin
* Player

**Cada quiz é composto por**:

* 10 perguntas com 3 respostas onde apenas 1 é correta.
* Cada resposta correta acumula a 1 ponto.
* Cada resposta errada perde 1 ponto. A menor pontuação possível é 0.
* Possui uma categoria.

**Ao iniciar o jogo**:

* O player deve escolher uma categoria válida e receber um quiz com perguntas aleatórias referentes a categoria escolhida.

**Ao finalizar o jogo**:

* O player deve receber a contabilização dos seus pontos juntamente com a sua posição atual no ranking global. Não há limitação de quantos quizzes o player pode responder.

**O ranking global**:

* É a contabilização dos pontos acumulados por cada player.
* Ranking geral considera todas as categorias.
* Ranking por categoria agrupa por categorias.

**Permissões**:

* Todos os endpoints devem estar protegidos por autenticação.
* Usuários do tipo **Admin** tem permissão para criar perguntas e respostas para os quizzes.
* Usuários do tipo **Player** tem permissão para jogar e consultar o ranking.

## Requisitos

* O projeto precisa estar configurado para rodar em um ambiente macOS ou Ubuntu (preferencialmente como container Docker).
* Deve anexar ao seu projeto uma coleção do postman com todos os endpoints criados e exemplos de utilização.

**Para executar seu código devemos executar apenas os seguintes comandos**:

* git clone $seu-fork
* cd $seu-fork
* comando para instalar dependências
* comando para executar a aplicação

## Critério de avaliação

* **Organização do código**: Separação de módulos, view e model
* **Clareza**: O README explica de forma resumida qual é o problema e como pode rodar a aplicação?
* **Assertividade**: A aplicação está fazendo o que é esperado? Se tem algo faltando, o README explica o porquê?
* **Legibilidade do código** (incluindo comentários)
* **Segurança**: Existe alguma vulnerabilidade clara?
* **Cobertura de testes** (Não esperamos cobertura completa mas é importante garantir o fluxo principal)
* **Histórico de commits** (estrutura e qualidade)
* **UX**: A API é intuitiva?
* **Escolhas técnicas**: A escolha das bibliotecas, banco de dados, arquitetura, etc, é a melhor escolha para a aplicação?

## Dúvidas

Quaisquer dúvidas que você venha a ter, consulte as issues para ver se alguém já não a fez e caso você não ache sua resposta, abra você mesmo uma nova issue!

Ao completar o desafio, submeta um pull-request a esse repositório com uma breve explicação das decisões tomadas e principalmente as instruções para execução do projeto.

**Boa sorte! ;)**
