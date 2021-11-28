from user_auth.models.profiles import CustomUser
from django.core.management.base import BaseCommand, CommandError
from desafio_config.settings import ADMINS,DEFAULT_PW
# from django.contrib.auth.models import User
from quiz.models.quiz import * 
from quiz.models.question import *
import json 
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

class Command(BaseCommand):
    help = 'Create Base admin users'
    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def process_questions(self,questions,category):
        for item in questions:
            enunciation = item['enunciation']
            question,created = Question.objects.get_or_create(enunciation=enunciation,quiz=category)
            
            if created:
                map(lambda x: Option.objects.create(**x),item['options'])
            


    def handle(self, *args, **options):

        try:
            with open(f'{dir_path}/questions.json','r') as f:
                data = json.load(f)

            f.close()

            quizes = Quiz.objects.all()
            print(quizes.values('category'))
            for item in data:
                
                category = quizes.get(category=item['category'])
                questions = item['questions']
                self.process_questions(questions,category)

            
        except Exception as e:
            raise CommandError( e)
        self.stdout.write(self.style.SUCCESS('Successfully read quiz json'))