from django.core.management.base import BaseCommand, CommandError
import json 
from quiz.models.quiz import *
from .utils import dir_path


class Command(BaseCommand):
    help = 'Create quiz'
    
    def handle(self, *args, **options):

        try:
            # open json file with quiz content

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