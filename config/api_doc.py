from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions

description = 'Valora Quiz'

info = openapi.Info(title='Valora quiz',
                    default_version='v1',
                    description=description,
                    terms_of_service='https://www.google.com/policies/terms/',
                    contact=openapi.Contact(
                        name='Diego Marcelino',
                        url='https://www.linkedin.com/in/diegomarcelino/'),
                    license=openapi.License(name='MIT License'))

schema_view = get_schema_view(info=info,
                              public=True,
                              permission_classes=[permissions.AllowAny],
                              authentication_classes=())

swagger_view = schema_view.with_ui('swagger', cache_timeout=0)
redoc_view = schema_view.with_ui('redoc', cache_timeout=0)
