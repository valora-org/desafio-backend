"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.admin import site
from django.urls import include, path

urlpatterns = [
    path('admin/', site.urls),
    path('accounts/', include('accounts.urls', namespace='account')),
    path('answers/', include('answers.urls', namespace='answer')),
    path('categories/', include('categories.urls', namespace='category')),
    path('questions/', include('questions.urls', namespace='question')),
    path('quizzes/', include('quizzes.urls', namespace='quiz')),
]
