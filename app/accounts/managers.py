from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
	"""
		Class to create custom user.
		Each user has its username and password.
		Can be player or administrator.

	"""
	def _create_user(self, username, password, **extra_fields):
		"""
			Function to create user.
			Each user has its username and password.

		"""
		user = self.model(username=username, **extra_fields)
		user.set_password(password)
		user.full_clean()
		user.save()
		return user

	def create_user(self, username, password, **extra_fields):
		"""
			Function to create player.
	
		"""
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(username, password, **extra_fields)

	def create_superuser(self, username, password, **extra_fields):
		"""
			Function to create admin.
	
		"""
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have staff priviledges')
		return self._create_user(username, password, **extra_fields)


