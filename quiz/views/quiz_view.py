# from user_auth.serializers.profiles_ser import * 
from user_auth.permissions import *
from quiz.models.quiz import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from desafio_config.utils.views import MixedPermissionModelViewSet
from rest_framework.permissions import *
from rest_framework.decorators import action
from django.http import JsonResponse
from quiz.serializers import *

class QuizViewset(MixedPermissionModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permissions_classes = [IsPlayer]
    permission_classes_by_action = {'list': [IsPlayer],
                                    'create': [AllowAny],
                                    'retrieve': [IsPlayer],
                                    'destroy': [IsAdminUser],
                                    'update': [IsAdminUser],
                                    'partial_update': [IsAdminUser],
                                    }
    
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        user = self.request.user
        query_set = self.queryset
        return query_set.filter(pk=user.id)
    
    # @action(['GET'],detail=False,permissions_classes=[IsPlayer])
    # def get_categories(self,request,pk=None):
    #     items = self.queryset
    #     ser = QuizCategoriesGetSimpleSerializer(items)

    #     return JsonResponse(
    #         ser.data,safe=False
    #     )
    

    # @action(['GET'],detail=True,permissions_classes=[IsPlayer])
    # def questions(self,request,pk=None):
    #     instance = self.get_object()

    #     questions = instance.questions.all()

    #     ser = QuestionGetSimpleSerializer(questions)

    #     return JsonResponse(
    #         ser.data,safe=False
    #     )
    

    # @action(['POST'],detail=True,permissions_classes=[IsPlayer])
    # def send_answers(self,request,pk=None):
    #     instance = self.get_object()
    #     data = request.data
    #     context = {'request':request,"quiz":instance}
    #     ser = QuestionAnswerSerializer(data=data,context=context)
    #     ser.is_valid(raise_exception=True)
    #     ser.save()
        
    #     return JsonResponse(
    #         ser.data,safe=False
    #     )