from user_auth.models.profiles import CustomUser
from django.core.management.base import BaseCommand, CommandError
from desafio_config.settings import ADMINS,DEFAULT_PW
# from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create Base admin users'
    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        for email in ADMINS:
       
            try:
                admin = CustomUser.objects.create_superuser(
                    email=email[1],
                    username=email[1],
                    password=DEFAULT_PW,
                    is_superuser=True,
                    is_staff=True,
                    # user_type='Admin'
                    # password_confirm=DEFAULT_PW
                )
        
            except Exception as e:
                raise CommandError( e)
            self.stdout.write(self.style.SUCCESS('Successfully admin poll "%s"' % admin.id))