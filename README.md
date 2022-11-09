Uma breve explicação sobre o desafio:

Olá, Cleiton e Caio. 

Desenvolvi um DER que ajuda a mapear melhor o projeto. 
Há também a documentação em Swagger e Redoc, cujas URL's encontram-se em core/urls.py. 
Criei 49 testes de integração, os quais cobrem 87% da aplicação. Podem ser vistos inclusive no repositório remoto em função do uso do GitHub Actions. 

Surgiram algumas dúvidas, especialmente nos 2 últimos dias. Procurei nas issues, mas não achei. Considerando que algumas levaram um certo tempo para serem respondidas, optei por não abrir uma nova porque queria implementar algumas funcionalidades que ainda restavam. Acredito não ter faltado muito para implementar totalmente o que fora solicitado neste README. 

Sobre o workspace do Postman, peço desculpas por não fazê-lo necessariamente com ele, e sim com o Insomnia, por não estar familiarizado com aquele. Também porque priorizei a realização dos testes no curto espaço de tempo que faltava. Além do fato da própria documentação em Swagger permitir realizar as operações que Insomnia e Postman executam. Tenham certeza de que procurei fazer o meu melhor, o que, ainda assim, certamente está bem aquém daquilo que desenvolvedores seniores como vocês conseguem desenvolver.

Muito obrigado pela atenção dispensada em nossa conversa há 1 semana e pela oportunidade de realizar este teste!  

Atenciosamente,  
Leandro Medeiros

# Desafio Backend Python  

Parabéns! Se você chegou até aqui significa que você passou pelas etapas mais difíceis do nosso processo seletivo. Somos extremamente criteriosos com as pessoas que vão integrar nosso time porque só aceitamos pessoas incríveis!

Agora é a parte fácil. Chegou a hora de mostrar todas as suas habilidades de transformar café em código. Vamos lá?

Nesse desafio iremos avaliar suas habilidades em:

* **Python**
* **Django**
* **Django REST Framework**
* **Pytest** (desejável mas não obrigatório)
* **Docker** (desejável mas não obrigatório)

Você irá desenvolver a API de uma aplicação para a criação de um quiz de perguntas e respostas!

**A aplicação deverá prover o registro e autenticação de dois tipos de usuários**:

* Admin
* Player

**Cada quiz é composto por**:

* 10 perguntas com 3 respostas onde apenas 1 é correta.
* Cada resposta correta acumula 1 ponto.
* Cada resposta errada perde 1 ponto. A menor pontuação possível é 0.
* Possui uma categoria.

**Ao iniciar o jogo**:

* O player deve escolher uma categoria válida e receber um quiz com perguntas aleatórias referentes à categoria escolhida.

**Ao finalizar o jogo**:

* O player deve receber a contabilização dos seus pontos juntamente com a sua posição atual no ranking global. Não há limitação de quantos quizzes o player pode responder.

**O ranking**:

* É a contabilização dos pontos acumulados por cada player.
* Ranking geral considera todas as categorias.
* Ranking por categoria agrupa por categorias.
* Este requisito é desejável mas não obrigatório.

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
* **Cobertura de testes** (Não esperamos cobertura completa, mas é importante garantir o fluxo principal)
* **Histórico de commits** (estrutura e qualidade)
* **UX**: A API é intuitiva?
* **Escolhas técnicas**: A escolha das bibliotecas, banco de dados, arquitetura, etc, é a melhor escolha para a aplicação?

## Dúvidas

Quaisquer dúvidas que você venha a ter, consulte as issues para ver se alguém já não a fez e caso você não ache sua resposta, abra você mesmo uma nova issue!

Ao completar o desafio, submeta um pull-request a esse repositório com uma breve explicação das decisões tomadas e principalmente as instruções para execução do projeto.

**Boa sorte! ;)**
