from django import forms

from .models import words


class WordForm(forms.ModelForm):

     class Meta:
         model = words
         fields = ['word','meaning','example_1','example_2']