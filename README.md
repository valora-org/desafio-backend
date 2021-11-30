##  Desafio Backend Python - William Elias Alves

A seguir temos a descrição geral da aplicação , contendo as habilidades usadas e descrições de execução de código.


### Requisitos Funcionais

**Cada quiz é composto por**:

* 10 perguntas com 3 respostas onde apenas 1 é correta.
* Cada resposta correta acumula a 1 ponto.
* Cada resposta errada perde 1 ponto. A menor pontuação possível é 0.
* Possui uma categoria.

**Ao iniciar o jogo**:

* O player deve escolher uma categoria válida e receber um quiz com perguntas aleatórias referentes a categoria escolhida.

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


### Requisitos de SO

* O projeto precisa estar configurado para rodar em um ambiente macOS ou Ubuntu (preferencialmente como container Docker).
* Deve anexar ao seu projeto uma coleção do postman com todos os endpoints criados e exemplos de utilização.

### Diagrama de classes

![Alt text](https://github.com/williamelias/desafio-backend/blob/dev/class_diagram.png)


### Execução

**Para executar seu código devemos executar apenas os seguintes comandos**:

* git clone $desafio-backend
* cd $desafio-backend
* instalar dependências e popular base: **sh build.sh**
* rodar os testes : **sh test.sh**
* executar a aplicação: **sh execute.sh**

**accessso admin**: admin@valora.com / a#dM10]ddln

***

### Pendências

* validação de única opção selecionada - Formulário de criação de questão (Admin) 
* validação de existência da resposta na lista de options - Question answer serializers (send_answer)
