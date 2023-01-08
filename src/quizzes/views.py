from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from quizzes.utils import Quizzes

class PlayQuizz(APIView):
    # TODO Add Player Permissions
    permission_required = ["user.can_play"]
    
    def post(self, request):
        category = request.data.get('category')
        user = request.user
        if not user.current_quizz:
            user.set_current_quizz(Quizzes(category=category).base_quizz)
            
        return Response(user.get_current_quizz_question())