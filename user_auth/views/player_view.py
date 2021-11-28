from django.shortcuts import render
from user_auth.serializers.profiles_ser import * 
from user_auth.permissions import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from desafio_config.utils.views import MixedPermissionModelViewSet
from rest_framework.permissions import *

class PlayerViewset(MixedPermissionModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
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