from rest_framework import serializers
from .models import Quiz, Question, Category, ANSWER_METHOD
from user.models import User, Point


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuestionSerializerToStartQuiz(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
          'id',
          'question',
          'answer_A',
          'answer_B',
          'answer_C'
        ]


class CategoryCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
        )
        read_only_fields = [
            'id',
        ]


class QuizCreateSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = (
            'id',
            'title',
            'category',
            'question',
        )
        read_only_fields = [
            'id',
        ]

    def create_questions(self, questions, quiz):
        for row in questions:
            question = Question.objects.create(**row)
            quiz.question.add(question)

    def create(self, validated_data):
        questions_objects = validated_data['question']
        del validated_data['question']
        quiz = Quiz.objects.create(**validated_data)
        self.create_questions(questions_objects, quiz)
        return quiz


class QuizListRetrieveSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = (
            'id',
            'title',
            'category',
            'question',
        )


class StartQuizSerializer(serializers.ModelSerializer):
    question = QuestionSerializerToStartQuiz(many=True)

    class Meta:
        model = Quiz
        fields = (
            'id',
            'title',
            'category',
            'question',

        )

        read_only_fields = [
            'id',
            'title',
            'question'
        ]


class FinishQuizSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())
    question_answers = serializers.ListField()
    correct_answers = serializers.ListField(read_only=True)
    quiz_id = serializers.IntegerField(write_only=True)
    global_points = serializers.IntegerField(read_only=True)

    class Meta:
        model = Quiz
        fields = (
            'user_id',
            'quiz_id',
            'question',
            'question_answers',
            'correct_answers',
            'global_points',
        )

    def create(self, validated_data):
        list_questions = []
        list_correct_answers = []
        quiz_points = 0
        global_points = 0
        index_answer = 0
        last_category_point = 0

        try:
            quiz_object = Quiz.objects.get(id=validated_data['quiz_id'])
        except:
            raise serializers.ValidationError(
                {'Erro': 'Quiz instance does not exists'})
        category_id = quiz_object.category.id
        user_id = validated_data['user_id'].id
        questions_answers = validated_data['question_answers']
        questions = validated_data['question']

        if not questions_answers.__len__() == 10 or not questions.__len__() == 10:
            raise serializers.ValidationError(
                {'validation_error': 'Please fill all 10 answers and questions on list.'})

        for letter in questions_answers:
            if letter not in ANSWER_METHOD:
                raise serializers.ValidationError(
                    {'validation_error': 'Type of answer: A/a, B/b, C/c.'})
        questions_answers = [each_string.upper() for each_string in questions_answers]

        for question in quiz_object.question.values():
            list_questions.append(question['id'])

        for question in questions:
            if question.id not in list_questions:
                raise serializers.ValidationError(
                    {'validation_error': f'Inexistent id:{question.id} on this quiz.'})
            question_object = Question.objects.get(id=question.id)
            list_correct_answers.append(question_object.correct_letter)
            if question_object.correct_letter == questions_answers[index_answer]:
                quiz_points = quiz_points + 1
            else:
                quiz_points = quiz_points - 1

            index_answer = index_answer + 1
        if quiz_points <= 0:
            quiz_points = 0

        user_object = User.objects.get(id=user_id)
        if user_object.points.values():
            for row in user_object.points.values():
                if row["category"] == category_id:
                    last_category_point = row["points"]
                    Point.objects.filter(id=row["id"]).delete()
            quiz_points = quiz_points + last_category_point

        point_object = Point.objects.create(points=quiz_points, category=category_id)
        user_object.points.add(point_object)
        final_user_object = User.objects.get(id=user_id)

        if final_user_object.points.values():
            for row in final_user_object.points.values():
                global_points = global_points + row["points"]
        else:
            global_points = quiz_points

        validated_data['question_answers'] = questions_answers
        validated_data['correct_answers'] = list_correct_answers
        validated_data['global_points'] = global_points
        Point.objects.filter(id=point_object.id).update(global_point=global_points)
        return validated_data


class QuizUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = (
            'id',
            'title',
            'category',
            'question',
        )
        read_only = [
            'id'
        ]

