from django.shortcuts import get_object_or_404
from rest_framework import status,viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from questao.models import Questao
from questao.serializers import QuestaoSerializer


class QuestaoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Questao.objects.all()
    serializer_class = QuestaoSerializer
    # def post(self,request):
    #     serializer = QuestaoSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    #     return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    # 
    # def delete(self,request, id=None):
    #     item = get_object_or_404(Questao, id=id)
    #     item.delete()
    #     return Response({"status": "successo", "data": "Registro deletado"},status=status.HTTP_200_OK)