# from user_auth.serializers.profiles_ser import * 
from user_auth.permissions import *
from quiz.models.quiz import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from desafio_config.utils.views import MixedPermissionModelViewSet
from rest_framework.permissions import *
from rest_framework.decorators import action
from django.http import JsonResponse
from quiz.serializers import *
from desafio_config.utils.auth import PlayerAuth 

class QuizViewset(MixedPermissionModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes_by_action = {'list': [IsPlayer],
                                    'create': [AllowAny],
                                    'retrieve': [IsPlayer],
                                    'destroy': [IsAdminUser],
                                    'update': [IsAdminUser],
                                    'partial_update': [IsAdminUser],
                                    }
    
    authentication_classes = [PlayerAuth]

   
    
    # @action(['GET'],detail=False,permissions_classes=[IsPlayer])
    # def get_categories(self,request,pk=None):
    #     items = self.queryset
    #     ser = QuizCategoriesGetSimpleSerializer(items)

    #     return JsonResponse(
    #         ser.data,safe=False
    #     )
    

    @action(['GET'],detail=True,permission_classes=[IsPlayer])
    def questions(self,request,pk=None):
        instance = self.get_object()

        questions = instance.questions.all()

        #verify if quiz questions is complete
        if not questions.count() >= 10:
            return JsonResponse(
                {'error':"Item não disponível"}
            )
        questions = random.choices(questions, k=10)
        ser = QuestionGetSimpleSerializer(questions,many=True)

        return JsonResponse(
            ser.data,safe=False
        )
    

    @action(['POST'],detail=True,permission_classes=[IsPlayer])
    def send_answers(self,request,pk=None):
        instance = self.get_object()
        data = request.data
        context = {'request':request,"quiz":instance}
        ser = QuizQuestionAnswerSerializer(data=data,context=context)
        ser.is_valid(raise_exception=True)
        saved = ser.save()
        
        return JsonResponse(
            saved,safe=False
        )