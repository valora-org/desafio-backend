from rest_framework.exceptions import APIException
from rest_framework.views import status


class UniqueException(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = 'this value must be unique'
