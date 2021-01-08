from django.http import JsonResponse


def match(request):
    if request.method == 'GET':
        player = {'id': 1, 'nome': 'Guilherme'}
        return JsonResponse(player)
