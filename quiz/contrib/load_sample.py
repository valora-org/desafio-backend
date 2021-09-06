from django.contrib.auth import get_user_model
from quiz.core.models import Category, Question

def create_user(username, password, is_admin=False):
    UserModel = get_user_model()
    if not UserModel.objects.filter(username=username).exists():
        user=UserModel.objects.create_user(username, password=password)
        user.is_superuser=is_admin
        user.is_staff=is_admin
        user.save()

def categories():
    for n in range(3):
        obj = Category(category=f'C{n+1}')
        obj.save()
    return Category.objects.all()

def create_questions():
    for category in categories():
        for n in range(10):
            obj = Question(
                category = category,
                question =f'Q{n+1}',
                answer1 = 'A1',
                answer2 = 'A2',
                answer3 = 'A3',
                right_answer = 'A1'
                )
            obj.save()
    return Question.objects.all()

if __name__ == '__main__':
    create_user('admin', '1', True)
    create_user('player', '1')
    create_questions()
    