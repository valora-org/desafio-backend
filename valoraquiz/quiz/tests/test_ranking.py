from quiz import models, services

from . import base


class RankingBaseTest(base.RestBaseTest):
    def setUp(self):
        super().setUp()

        self.category = self.create_fake_category(title="Category1")

    def build_questions(self, category):
        count = 0
        while count <= 10:
            question = self.create_fake_question(
                label=f"Question {count}", category=category
            )
            for idx in range(3):
                self.create_fake_answer(
                    label=f"Answer {idx}",
                    question=question,
                    is_right=False if idx < 2 else True,
                )
            count += 1

    def answered_quiz(self, quiz, is_finished=True, force_win=False):
        for question in quiz.questions.all():
            if force_win:
                answer = question.answer_set.filter(is_right=True).get()
            else:
                answer = question.answer_set.all().order_by("?").first()

            if answer:
                quiz.answers.add(answer)

        quiz.is_finished = is_finished
        quiz.save()


class RankingTest(RankingBaseTest):
    def test_get_ranking_by_category(self):
        self.build_questions(self.category)

        quiz1 = services.create_quiz(
            category_id=self.category.pk, user=self.user_player
        )
        self.answered_quiz(quiz1, force_win=True)

        quiz2 = services.create_quiz(category_id=self.category.pk, user=self.user_admin)
        self.answered_quiz(quiz2)

        self.auth()
        response = self.client.get(f"/api/ranking/{self.category.pk}/")
        self.assertEquals(response.status_code, 200)

        ranking = response.json()
        self.assertTrue(
            ranking[0][self.user_player.username]  # player is top1
            > ranking[1][self.user_admin.username]
        )

    def test_get_ranking_global(self):
        self.build_questions(self.category)
        category = self.create_fake_category(title="Category")
        self.build_questions(category)

        quiz1 = services.create_quiz(category_id=category.pk, user=self.user_player)
        self.answered_quiz(quiz1, force_win=True)
        quiz2 = services.create_quiz(
            category_id=self.category.pk, user=self.user_player
        )
        self.answered_quiz(quiz2, force_win=True)

        quiz3 = services.create_quiz(category_id=self.category.pk, user=self.user_admin)
        self.answered_quiz(quiz3, force_win=True)

        self.auth()
        response = self.client.get(f"/api/ranking/")
        self.assertEquals(response.status_code, 200)

        ranking = response.json()
        self.assertEquals(ranking[0][self.user_player.username], 20)
        self.assertEquals(ranking[1][self.user_admin.username], 10)
        self.assertTrue(  # player is top1 from two categories
            ranking[0][self.user_player.username] > ranking[1][self.user_admin.username]
        )
