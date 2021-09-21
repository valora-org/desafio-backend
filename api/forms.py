from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email']


class UserAdminForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'is_active', 'is_staff']