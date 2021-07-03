from django import forms

from .models import words


class WordForm(forms.ModelForm):

     class Meta:
         model = words
         fields = '__all__'