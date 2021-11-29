from django import forms 
from quiz.models.question import *

class QuestionForm(forms.ModelForm):
    
    class Meta:
        model = Question 
        fields = "__all__"

  
    def clean(self):
        cleaned =  super().clean()  
        return cleaned
    
 
    def save(self, commit: False):
        
        saved = super().save(commit=commit)
        return saved