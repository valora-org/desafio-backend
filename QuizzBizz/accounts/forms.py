from accounts.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserCreationForm(UserCreationForm):
		
		#Form to created new users.


	class Meta(UserCreationForm):
		model = User
		fields = ('username',)


class UserChangeForm(UserChangeForm):

	#Custom form to created new users.

	class meta:
		model = User
		fields = ('email', 'username')