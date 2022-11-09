from django.core.management.base import BaseCommand
from ...models import User
from django.db import IntegrityError


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        help = "Creates a default admin"

        try:

            admin = User.objects.create_superuser(
                email="admin@admin.com", username="admin", password="P4ssw0rD"
            )
            self.stdout.write(self.style.SUCCESS("Default admin created"))

        except IntegrityError:
            self.stdout.write(self.style.WARNING("Default admin already exists"))
