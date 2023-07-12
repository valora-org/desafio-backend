from rest_framework import viewsets, permissions
from rest_framework.response import Response
from quiz.models import Quiz, Question, Answer
from quiz.serializers import QuizSerializer, QuestionSerializer, AnswerSerializer, RankingSerializer
from django.core.exceptions import PermissionDenied, ValidationError
from accounts.models import CustomUser as User
from rest_framework.parsers import JSONParser

class AdminPermission(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    max_num = None

    def create(self, request, *args, **kwargs):
        if request.user.is_staff:
            if self.max_num is not None:
                """
                Used to create model instance with maximum value
                """
                if isinstance(self.max_num, int) and self.max_num > 0:
                    queryset = self.get_queryset()
                    existed_object = queryset.count()

                    if existed_object == self.max_num:
                        raise ValidationError("Maximum amount reached")
                    else:
                        return super().create(request, *args, **kwargs)
                
            else:
                return super().create(request, *args, **kwargs)    
            
        else:
            raise PermissionDenied()
        
    def update(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super().update(request, *args, **kwargs)
        else:
            raise PermissionDenied()
        
    def destroy(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super().destroy(request, *args, **kwargs)
        else:
            raise PermissionDenied()
        
    def get_max_num(self, request, obj=None, **kwargs):
        """
        Used to set get max quantity of objects to create
        """
        return self.max_num
        
    


   
class QuizView(AdminPermission):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    
    
    def retrieve(self, request, format=None, **kwargs):
        """
        Return list of 10 questions of specific quiz
        """
        question = Question.objects.filter(category_id=kwargs["pk"]).order_by("?")[:10]
        serializer = QuestionSerializer(question, context={'request': request}, many=True)
        return Response(serializer.data)
    
    
    
    
    

class QuestionView(AdminPermission):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
    
    
            
    

class AnswerView(AdminPermission):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def increase_score(self):
        user_score = User.score
        if user_score >= 0:
            user_score = user_score + 1
        return user_score
    
    def decrease_score(self):
        user_score = User.score
        if user_score > 0:
            user_score = user_score - 1
        else:
            user_score = user_score
        return user_score

    def validate_correct_answer(self, request):
        """
        Used to check with the player hit the correct answer
        """
        useranswer = JSONParser().parse(request)
        serializer = AnswerSerializer(data=useranswer)
        if serializer.is_valid(raise_exception=True):
            question_answer = Answer.objects.get(pk = useranswer["pk"])
            if question_answer.is_correct == useranswer["is_correct"]:
                self.increase_score()
            else:
                self.decrease_score()
            
class RankingView(viewsets.ReadOnlyModelViewSet):
    """
    List all player with decreasing score
    """
    queryset = User.objects.all().order_by("-score")
    serializer_class = RankingSerializer
    permission_classes = [permissions.AllowAny]