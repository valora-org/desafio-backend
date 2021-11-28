from django import forms 
from quiz.models.question import *

class QuestionForm(forms.ModelForm):
    
    class Meta:
        model = Question 
        fields = "__all__"

  
    def clean(self):
        cleaned =  super().clean()  
        print(cleaned)
        return cleaned
    
 
    def save(self, commit: False):
        
        saved = super().save(commit=commit)
        print(saved)
        return saved