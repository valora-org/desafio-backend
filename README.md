
# Valora Challenge - Dev Backend Python - Marcelo

Olá, antes de tudo listarei oque está faltando:

- Arquivos do docker
- Testes unitários

Bom, não consegui fazer tudo que eu queria pela falta de tempo ( durante a semana trabalho ) e no 
final de semana que estava separando para me aprofundar mais nesses detalhes descritos acima e em
algumas partes especificas do codigo ( ranking / autenticação via token ) minha instalação do
Ubuntu deu problema me fazendo perder boa parte do tempo do fim de semana.

Dado o exposto aqui vai um resumo das minhas escolhas técnicas ( + peculiares no código ):

- Decidi fazer as choices / escolhas no modelo de perguntas como um campo ChoiceField por motivos de economizar quantidades de acessos no banco

- A escolha do Quizz ser um JSONField no usuário foi feita tanto para agilizar o desenvolvimento ( Facilitar no enquadramento das regras exigidas ) quanto para reduzir numero de acessos no banco.

Vale ressaltar que por padrão a aplicação cria 2 usuários para motivo de facilitar o teste na migration, valoraPlayer@mail.com e valoraAdmin@mail.com
ambos com senha 123 e com as permissões de cada grupo.

## Passos para rodar a aplicação!

Baixe o projeto localmente e siga os passos seguintes

```bash
  git clone https://github.com/MarceloJDCB/desafio-backend.git
  
  cd desafio-backend/src
  python3 -m venv venv && source venv/bin/activate
  python3 -m pip install -r requirements.txt
  cd src
  python3 -m manage migrate
  python3 -m manage runserver

```
    
## Tutorial

- Obtenha o access_token na parte de login do postman, use o email valoraAdmin@mail.com para obter um usuário com permissão para criar categorias e questões. 
- Crie as questões ( o campo 'category' é o nome da categoria e o campo 'correct_choice' é a alternativa certa da questão, podendo variar entre as 3 ) você tem que criar no minimo 10 da categoria criada para começar a jogar!

#### Tendo criado as perguntas, é hora de jogar! 
- Obtenha o token de acesso com o email valoraPlayer@mail.com, vá na request Get Quiz depois de configurar o Bearer token na aba de autenticação do Postman e passe o campo 'category' para obter um quiz para seu usuário ( o endpoint irá retornar uma pergunta aleatória do mesmo )
- Para responder a pergunta que você recebeu no endpoint anterior vá para a request Play Quiz e passe o campo 'answer_choice' com a escolha que você acha correta ( first , second ou third | choice) 
- Vale ressaltar que você consultar o ranking da categoria que você jogou acessando o endpoint consult_category_ranking e passando o campo 'category' para ele, ou se preferir pode acessar o ranking global apenas acessando o endpoint consult_global_ranking
