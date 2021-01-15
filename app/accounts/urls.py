from accounts.views import Login, Create
from django.urls import path

# URLs to access as accounts endpoints
urlpatterns = [
	path("login/", Login.as_view()),
	path("create/", Create.as_view())
]