from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

class QuizViewMixin(APIView, PermissionRequiredMixin):
    
    def dispatch(self, request, *args, **kwargs):
        
        self.args = args
        self.kwargs = kwargs
        request = self.initialize_request(request, *args, **kwargs)
        self.request = request
        self.headers = self.default_response_headers  # deprecate?
        
        if not self.has_permission():
            return self.handle_no_permission()

        try:
            self.initial(request, *args, **kwargs)

            # Get the appropriate handler method
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(),
                                  self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed

            response = handler(request, *args, **kwargs)

        except Exception as exc:
            response = self.handle_exception(exc)

        if request.method == 'POST' and self.serializer_class:
            serializer = self.serializer_class(data=request.data)
            if not serializer.is_valid():
                response = Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        self.response = self.finalize_response(request, response, *args, **kwargs)
        return self.response


class QuizPlayViewMixin(QuizViewMixin, CreateAPIView):
    
    permission_required = ["accounts.can_play"]
    permission_denied_message = 'Usuário sem permissão para jogar um Quiz'
    serializer_class = None
    
class QuizCreationViewMixin(QuizViewMixin, CreateAPIView):
    
    permission_required = ["quizzes.can_create_category", "quizzes.can_create_question"]
    permission_denied_message = 'Usuário sem permissão para criar um Quiz'
    serializer_class = None
   
