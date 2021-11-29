
from django.core.exceptions import ValidationError
from user_auth.models import Player
from rest_framework_simplejwt.authentication import *
from django.utils.translation import gettext as _

class PlayerAuth(JWTAuthentication):
    """
    Override default jwt authentication user
    New jwt user is Player and admin_user is DjangoUser
    """

    def get_user(self, validated_token):
        try:
            user_id = validated_token['user_id']
        except KeyError:
            raise InvalidToken(
                'Token contained no recognizable user identification')

        try:
            user = Player.objects.get(id=user_id)
            return user
        except Player.DoesNotExist:
            raise AuthenticationFailed(
                _('User not found'), code='user_not_found')
        except ValidationError:
            raise AuthenticationFailed(
                _('Authentication Failed'), code='error_process_code')
