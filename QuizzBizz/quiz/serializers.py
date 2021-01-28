from quiz.models import Quiz, QuizTaker, Question, Answer, UsersAnswer
from accounts.models import User
from accounts.serializers import UserSerializer
from rest_framework import serializers



class QuizListSerializer(serializers.ModelSerializer):

	#serializer to return the name, id, image, slug, questions_count of the model quiz
	
	questions_count = serializers.SerializerMethodField()
	class Meta:
		model = Quiz
		fields = ["id", "name", "description", "image", "slug", "questions_count", ]
		read_only_fields = ["questions_count"]


	def get_questions_count(self, obj):
		return obj.question_set.all().count()


class AnswerSerializer(serializers.ModelSerializer):

	#serializer to return, id, question and label of the model answer

	class Meta:
		model = Answer
		fields = ["id", "question", "label"]


class QuestionSerializer(serializers.ModelSerializer):

	#serializer to return, all of the model Question

	answer_set = AnswerSerializer(many=True)

	class Meta:
		model = Question
		fields = "__all__"


class UsersAnswerSerializer(serializers.ModelSerializer):

	#serializer to return, all of the model UsersAnswer

	class Meta:
		model = UsersAnswer
		fields = "__all__"


class MyQuizListSerializer(serializers.ModelSerializer):

	#Serializer to return id, name, category, score of the player.

	completed = serializers.SerializerMethodField()
	progress = serializers.SerializerMethodField()
	questions_count = serializers.SerializerMethodField()
	score = serializers.SerializerMethodField()
	

	class Meta:
		model = Quiz
		fields = ["id", "name", "description", "image", "slug", "questions_count", "completed", "score", "progress",]
		read_only_fields = ["questions_count", "completed", "progress"]

	def get_completed(self, obj):
		try:
			quiztaker = QuizTaker.objects.get(user=self.context['request'].user, quiz=obj)
			return quiztaker.completed
		except QuizTaker.DoesNotExist:
			return None

	def get_progress(self, obj):
		try:
			quiztaker = QuizTaker.objects.get(user=self.context['request'].user, quiz=obj)
			if quiztaker.completed == False:
				questions_answered = UsersAnswer.objects.filter(quiz_taker=quiztaker, answer__isnull=False).count()
				total_questions = obj.question_set.all().count()
				return int(questions_answered / total_questions)
			return None
		except QuizTaker.DoesNotExist:
			return None

	def get_questions_count(self, obj):
		return obj.question_set.all().count()

	def get_score(self, obj):
		try:
			quiztaker = QuizTaker.objects.get(user=self.context['request'].user, quiz=obj)
			if quiztaker.completed == True:
				return quiztaker.score
			return None
		except QuizTaker.DoesNotExist:
			return None
	
	def get_category(self, obj):
		
			#Return category of the quiz.
		
		try:
			category = Category.objects.get(quiz=obj)
			serializer = CategorySerializer(category)
			return serializer.data


		except Category.DoesNotExist:
			return None


class QuizTakerSerializer(serializers.ModelSerializer):

		#Serializer to return all fields of the model QuizTaker.

	usersanswer_set = UsersAnswerSerializer(many=True)

	class Meta:
		model = QuizTaker
		fields = "__all__"


class QuizDetailSerializer(serializers.ModelSerializer):

		#Serializer to return the quiz details obtained to the player.

	quiztakers_set = serializers.SerializerMethodField()
	question_set = QuestionSerializer(many=True)
		
	
	class Meta:
		model = Quiz
		fields = "__all__"

	def get_quiztakers_set(self, obj):
		try:
			quiz_taker = QuizTaker.objects.get(user=self.context['request'].user, quiz=obj)
			serializer = QuizTakerSerializer(quiz_taker)
			return serializer.data
		except QuizTaker.DoesNotExist:
			return None


class QuizResultSerializer(serializers.ModelSerializer):

	#Serializer to return the questions of quiz for player.

	quiztaker_set = serializers.SerializerMethodField()
	question_set = QuestionSerializer(many=True)

	class Meta:
		model = Quiz
		fields = "__all__"

	def get_quiztaker_set(self, obj):
		try:
			quiztaker = QuizTaker.objects.get(user=self.context['request'].user, quiz=obj)
			serializer = QuizTakerSerializer(quiztaker)
			return serializer.data

		except QuizTaker.DoesNotExist:
			return None 


class RankingSerializer(serializers.ModelSerializer):
	
		#Serializer to return all fields of the model QuizTaker, global ranking
		
	
	# Retrieval of the user.
	user = serializers.SerializerMethodField()
	# Retrieval of the quiz.
	quiz = serializers.SerializerMethodField()

	class Meta:
		model = QuizTaker
		fields = ["user", "quiz", "score"]

	def get_user(self, obj):
		
		#Return users.
		
		try:
			user = User.objects.get(quiztaker=obj)
			serializer = UserSerializer(user)
			return serializer.data

		except QuizTaker.DoesNotExist:
			return None 

	def get_quiz(self, obj):
		
		#Return quiz.
		
		try:
			quiz = Quiz.objects.get(quiztaker=obj)
			serializer = QuizListSerializer(quiz)
			return serializer.data


		except QuizTaker.DoesNotExist:
			return None 