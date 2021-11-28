
from django.core.exceptions import ValidationError
from user_auth.models import Player
from rest_framework_simplejwt.authentication import *
# from users.models import CustomUser as User
from django.utils.translation import gettext as _

class PlayerAuth(JWTAuthentication):

    def get_user(self, validated_token):
        try:
            user_id = validated_token['user_id']
        except KeyError:
            raise InvalidToken(
                'Token contained no recognizable user identification')

        try:
            user = Player.objects.get(id=user_id)
            print(user)
            print(type(user))
            return user
        except Player.DoesNotExist:
            raise AuthenticationFailed(
                _('User not found'), code='user_not_found')
        except ValidationError:
            # raise serializers.ValidationError({'error':"Wrong pattern"})
            # type_micro = validated_token['type_micro']
            # user_type = validated_token.get('user_type','default')
            # if not type_micro == 'verify' and user_type == 'default':
            raise AuthenticationFailed(
                _('Authentication Failed'), code='error_process_code')

            # return None

        # if isinstance(user, Player) and not user.user.is_active:
        #     raise AuthenticationFailed(
        #         _('User is inactive'), code='user_inactive')

        # return user


