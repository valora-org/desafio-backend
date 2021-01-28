from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from quiz.models import Answer, Question, Quiz, QuizTaker, UsersAnswer
from quiz.serializers import MyQuizListSerializer, QuizDetailSerializer, QuizListSerializer, QuizResultSerializer, UsersAnswerSerializer, RankingSerializer


class MyQuizListAPI(generics.ListAPIView):

	#View for the player to view their quizzes and scores.

	# Authetincation required
	permission_classes = [
		permissions.IsAuthenticated
	]

	# Respective serializer
	serializer_class = MyQuizListSerializer

	def get_queryset(self, *args, **kwargs):

		#GET method

		# Get all objects
		queryset = Quiz.objects.filter(quiztaker__user=self.request.user)
		query = self.request.GET.get("q")

		# Condition to differentiate by name
		if query:
			queryset = queryset.filter(
				Q(name__icontains=query) |
				Q(description__icontains=query)
			).distinct()

		# Return response
		return queryset


class QuizListAPI(generics.ListAPIView):

	#View for the player to view all quizzes.

	# Respective serializer
	serializer_class = QuizListSerializer
	
	# Authentication required
	permission_classes = [
		permissions.IsAuthenticated
	]

	def get_queryset(self, *args, **kwargs):

		#GET method

		# Get all objects
		queryset = Quiz.objects.filter(roll_out=True).exclude(quiztaker__user=self.request.user)
		query = self.request.GET.get("q")

		# Condition to differentiate by name
		if query:
			queryset = queryset.filter(
				Q(name__icontains=query) |
				Q(description__icontains=query)
			).distinct()

		# Return response
		return queryset


class QuizDetailAPI(generics.RetrieveAPIView):

	#View for the player to view all quiz details.

	# Respective serializer
	serializer_class = QuizDetailSerializer

	#Authentication Required
	permission_classes = [
		permissions.IsAuthenticated
	]

	# Get all objects
	def get(self, *args, **kwargs):
		slug = self.kwargs["slug"]
		quiz = get_object_or_404(Quiz, slug=slug)
		last_question = None
		obj, created = QuizTaker.objects.get_or_create(user=self.request.user, quiz=quiz)
		if created:
			for question in Question.objects.filter(quiz=quiz):
				UsersAnswer.objects.create(quiz_taker=obj, question=question)
		else:
			last_question = UsersAnswer.objects.filter(quiz_taker=obj, answer__isnull=False)
			if last_question.count() > 0:
				last_question = last_question.last().question.id
			else:
				last_question = None

		# Return response
		return Response({'quiz': self.get_serializer(quiz, context={'request': self.request}).data, 'last_question_id': last_question})


class SaveUsersAnswer(generics.UpdateAPIView):

	#View for the player to view Saved Users Answers.

	# Respective serializer
	serializer_class = UsersAnswerSerializer
	
	# Authentication required
	permission_classes = [
		permissions.IsAuthenticated
	]

	def patch(self, request, *args, **kwargs):

		#PATCH method

		quiztaker_id = request.data['quiztaker']
		question_id = request.data['question']
		answer_id = request.data['answer']

		quiztaker = get_object_or_404(QuizTaker, id=quiztaker_id)
		question = get_object_or_404(Question, id=question_id)
		answer = get_object_or_404(Answer, id=answer_id)

		#Quiztaker complete message
		if quiztaker.completed:
			return Response({
				"message": "This quiz is already complete. you can't answer any more questions"},
				status=status.HTTP_412_PRECONDITION_FAILED
			)
		
		# Save answer
		obj = get_object_or_404(UsersAnswer, quiz_taker=quiztaker, question=question)
		obj.answer = answer
		obj.save()

		# Return response
		return Response(self.get_serializer(obj).data)


class SubmitQuizAPI(generics.GenericAPIView):

	#View for the player to view submit answers.


	# Respective serializer
	serializer_class = QuizResultSerializer
	
	# Authentication required
	permission_classes = [
		permissions.IsAuthenticated
	]

	def post(self, request, *args, **kwargs):

		#POST method

		quiztaker_id = request.data['quiztaker']
		question_id = request.data['question']
		answer_id = request.data['answer']

		quiztaker = get_object_or_404(QuizTaker, id=quiztaker_id)
		question = get_object_or_404(Question, id=question_id)
		
		#get response
		quiz = Quiz.objects.get(slug=self.kwargs['slug'])

		#Quiztaker complete message
		if quiztaker.completed:
			return Response({
				"message": "This quiz is already complete. You can't submit again"},
				status=status.HTTP_412_PRECONDITION_FAILED
			)

		if answer_id is not None:
			answer = get_object_or_404(Answer, id=answer_id)
			obj = get_object_or_404(UsersAnswer, quiz_taker=quiztaker, question=question)
			obj.answer = answer
			obj.save()

		quiztaker.completed = True
		correct_answers = 0
		
		for users_answer in UsersAnswer.objects.filter(quiz_taker=quiztaker):
			answer = Answer.objects.get(question=users_answer.question, is_correct=True)
			print(answer)
			print(users_answer.answer)
			if users_answer.answer == answer:
				correct_answers += 1

		quiztaker.score = int(correct_answers / quiztaker.quiz.question_set.count() * 100)
		print(quiztaker.score)
		quiztaker.save()

		# Return response
		return Response(self.get_serializer(quiz).data)


class QuizRankingList(generics.ListAPIView):
	
		#View for the player to view overall ranking by quiz.
	

	# Authentication required
	permission_classes = [
		permissions.IsAuthenticated
	]

	# Respective serializer
	serializer_class = RankingSerializer

	def get_queryset(self, *args, **kwargs):
		
			#GET method
		

		# Get all objects
		queryset = QuizTaker.objects.filter(quiz__slug=self.kwargs['slug']).order_by("-score")

		# Return response
		return queryset

