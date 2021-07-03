from django.shortcuts import render,get_object_or_404

from django.http import HttpResponse
import json
from difflib import get_close_matches

#import models
from .models import words

#import forms
from .forms import WordForm
import ast


def homepage(request):
    
    with  ast.literal_eval(open('static/file/result.json', 'r', encoding='utf-8')) as jsonfile:
        data = json.load(jsonfile)
    
    '''for i in data:
        save_data = words.objects.create(word = i['Word'], meaning = i['Meaning'], example_1 = i["Examples/0"],
        example_2 = i["Examples/1"],example_3 = i["Examples/2"],example_4 = i["Examples/3"],example_5 = i["Examples/4"],
        example_6 = i["Examples/5"],example_7 = i["Examples/6"],example_8 = i["Examples/7"],example_9 = i["Examples/8"],
        example_10 = i["Examples/9"], ) '''
         
    return render(request, 'base.html', {"jsonfile":data})


def get_word(request):
    
    if request.method == "POST":
        gotten_word = request.POST.get("word")
        #get meanings
        try:
            word_gotten = words.objects.get(word = gotten_word.title())
            return render(request, 'get_word.html', {'word':word_gotten})
        except words.DoesNotExist:
            suggested_word = get_close_matches(gotten_word.title(), [i.word for i in words.objects.all()])[0]
            return render(request, 'get_word.html', {'suggested_word':suggested_word, 'gotten_word':gotten_word})
    return render(request, 'base.html')

def suggested_word_meaning(request, gotten_word):
    #get meanings
    try:
        word_gotten = words.objects.get(word = gotten_word.title())
        return render(request, 'get_word.html', {'word':word_gotten})
    except words.DoesNotExist:
        suggested_word = get_close_matches(gotten_word.title(), [i.word for i in words.objects.all()])[0]
        return render(request, 'get_word.html', {'suggested_word':suggested_word, 'gotten_word':gotten_word})
    