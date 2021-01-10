
from crispy_forms.helper import FormHelper
from django import forms
from django.forms import widgets


class QuizForm(forms.Form):

    def __init__(self, *args, **kwargs):
        questoes = kwargs.pop('questoes')  # pop questoes array from kwargs
        super().__init__(*args, **kwargs)
        if questoes:
            for question in questoes:  # add a form field for each question
                CHOICES = (
                    ('A', question. option_a),
                    ('B', question. option_b),
                    ('C', question. option_c),
                )
                self.fields[question.question] = forms.ChoiceField(required=False, choices=CHOICES,
                                                                           widget=widgets.RadioSelect)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    def answers(self):  # return questions and answers for result processing
        for name, question in self.cleaned_data.items():
            yield (name, question)
