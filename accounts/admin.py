from django.contrib.admin import site

from accounts.models import Account


site.register(Account)
