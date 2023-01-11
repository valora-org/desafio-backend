from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import Group, User
from quizzes.utils import Quizzes
from ranking import models as ranking_models
from django.db.models import Subquery, OuterRef, Sum

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    """
    Fully featured User model with admin-compliant permissions.

    Email and password are required. Other fields are optional.
    """

    admin_choice = "Admin"
    player_choice = "Player"
    TYPES_CHOICES = (
        (admin_choice, "Administrador"),
        (player_choice, "Jogador"),
    )

    first_name = models.CharField(_("first name"), max_length=30, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    current_quiz = models.JSONField(verbose_name="Quiz Atual", null=True, blank=True)
    user_type = models.CharField(verbose_name="Tipo de Usuário", default=player_choice, blank=True, choices=TYPES_CHOICES, max_length=50)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
    
    def __str__(self) -> str:
        return self.email

    def change_user_type(self):
        all_groups = Group.objects.all()
        if not self.user_type in self.groups.values_list("name", flat=True):
            self.groups.remove(*all_groups)
            self.groups.add(Group.objects.get(name=self.user_type))
        return self
        

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.change_user_type()
        save = super().save(*args, **kwargs)
        return save

    def get_ranking(self, category: str):
        return ranking_models.Ranking.objects.filter(player=self,category=category).first()

    def add_new_ranking(self, category: str):
        if not self.get_ranking(category):
            ranking = ranking_models.Ranking()
            ranking.player = self
            ranking.category = category
            ranking.save()

    def set_current_quiz(self, quiz):
        self.current_quiz = quiz
        self.add_new_ranking(self.current_quiz['category'])
        self.save()

    def get_random_question_from_current_quiz(self):
        quiz = Quizzes(quiz=self.current_quiz)
        self.set_current_quiz(quiz.randomize_quiz_questions())
        return quiz.get_first_quiz_question()
    
    def get_current_question_from_quiz(self):
        return Quizzes(quiz=self.current_quiz).get_first_quiz_question()
    
    def exclude_current_question_and_decrease_ranking_point(self):
        self.current_quiz['questions'].pop(0)
        self.decrease_ranking_point()
        num_question = len(self.current_quiz['questions'])
        if num_question == 0:
            self.current_quiz = ''
        self.save()
        return num_question
    
    def exclude_current_question_and_increase_ranking_point(self):
        self.current_quiz['questions'].pop(0)
        self.increase_ranking_point()
        num_question = len(self.current_quiz['questions'])
        if num_question == 0:
            self.current_quiz = ''
        self.save()
        return num_question

    def is_the_last_question(self):
        return len(self.current_quiz['questions']) == 1
    
    def increase_ranking_point(self):
        self.get_ranking(self.current_quiz['category']).increase_point()
        return self
    
    def decrease_ranking_point(self):
        self.get_ranking(self.current_quiz['category']).decrease_point()
        return self
    
    def position_in_ranking(self):
        return self.get_ranking(self.current_quiz['category']).position_in_ranking()
    
    @staticmethod
    def get_global_ranking():
        return User.objects.all().annotate(
            all_rank_points=Subquery(
                User.objects.filter(id=OuterRef('id'))
                .annotate(all_rank_points=Sum('ranking__points'))
                .values(
                    'all_rank_points'
                )
            )
        ).order_by('-all_rank_points')

    def position_in_global_ranking(self):
        global_rank_users = self.get_global_ranking()
        for position, ranking in enumerate(global_rank_users):
            if ranking == self:
                return position + 1

                                           
        