from user_auth.models.profiles import CustomUser
from django.core.management.base import BaseCommand, CommandError
from desafio_config.settings import ADMINS,DEFAULT_PW
# from django.contrib.auth.models import User
import json 
import os 
from quiz.models.quiz import *

dir_path = os.path.dirname(os.path.realpath(__file__))

class Command(BaseCommand):
    help = 'Create Base admin users'
    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):

        try:
            print(dir_path)

            with open(f'{dir_path}/quiz.json','r') as f:
                data = json.load(f)
            f.close()

            for item in data:
                try:
                    Quiz.objects.create(**item)
                except:
                    import traceback
                    traceback.print_exc()

        except Exception as e:
            raise CommandError( e)
        self.stdout.write(self.style.SUCCESS('Successfully read quiz json'))