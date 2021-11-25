from django.contrib.auth.models import User

from categoria.models import Categoria
from questao.models import Questao
from resposta.models import Resposta

try:
    print('******************INICIANDO INSERT USER*************')
    admin = User.objects.create_superuser('adminValora', None, password='1234')
    player = User.objects.create_user('playerValora', None, password='1234')

    print('******************INICIANDO INSERT CATEGORIA*************')
    categorias = ['Programação', 'Artes', 'IOT']
    categoriasModel = []
    for nomeCategoria in categorias:
        categoriasModel.append(Categoria.objects.create(nome=nomeCategoria))

    print('******************INICIANDO INSERT QUESTAO e Resposta*************')
    for categoria in categoriasModel:
        print(categoria)
        for i in range(1,11):
            p = f"Pergunta {i}?"
            questao = Questao.objects.create(texto=p, categoria=categoria)
            print(questao)
            for j in range(1,4):

                correta = (j == 3)
                resposta = Resposta.objects.create(texto=f"Resposta {j} da pergunta {i}", questao=questao,
                                        correta=correta)
                print(resposta)
except Exception as e:
    print("Error",e)

