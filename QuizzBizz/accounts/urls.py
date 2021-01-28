from accounts.api import LoginAPI, RegisterAPI, UserAPI
from django.urls import path

# URLs to access as accounts endpoints
urlpatterns = [
	path("login/", LoginAPI.as_view()),
	path("register/", RegisterAPI.as_view(), name='register-account'),
	path("user/", UserAPI.as_view())
]