from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

from quiz.models import Question


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sequential = models.IntegerField(blank=True, default=1)
    question_correct = models.ManyToManyField(Question, related_name='question_correct', blank=True)
    question_wrong = models.ManyToManyField(Question, related_name='question_wrong', blank=True)
    points = models.IntegerField(blank=True, default=0)
    temp_points = models.IntegerField(blank=True, default=0)
    total_points = models.IntegerField(blank=True, default=0)

    def adicionar_points(self):
        self.total_points += 1
        self.save()

    def remove_points(self):
        self.total_points -= 1
        self.save()

    def att_sequential(queryset):
        sequential = 1
        for item in queryset:
            item.sequential = sequential
            item.save()
            sequential += 1

    def negativos_pontos(soma):
        if soma >= 0:
            return soma
        else:
            return 0

    def att_pontuacao(category_id, category=False):
        queryset = UserProfile.objects.all().order_by('-points', 'user__username').distinct()
        for item in queryset:
            pontos_q_certas = UserProfile.objects.filter(question_correct__category__id=category_id, user=item.user)
            pontos_q_erradas = UserProfile.objects.filter(question_wrong__category__id=category_id, user=item.user)
            soma = pontos_q_certas.count() - pontos_q_erradas.count()
            if category:
                item.points = UserProfile.negativos_pontos(soma)
                item.save()
            else:
                item.points = UserProfile.negativos_pontos(item.total_points)
                item.save()


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)
