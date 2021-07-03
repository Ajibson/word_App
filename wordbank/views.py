from django.shortcuts import render,redirect

from django.http import HttpResponse
import json
from difflib import get_close_matches

#import models
from .models import words

#import forms
from .forms import WordForm
import ast


def create_words(request):
    with open('static/file/result.json', 'r', encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)

    for i in data:
        try:
            save_data = words.objects.create(word = i['Word'], meaning = i['Meaning'], example_1 = i["Examples/0"],
            example_2 = i["Examples/1"],example_3 = i["Examples/2"],example_4 = i["Examples/3"],example_5 = i["Examples/4"],
            example_6 = i["Examples/5"],example_7 = i["Examples/6"],example_8 = i["Examples/7"],example_9 = i["Examples/8"],
            example_10 = i["Examples/9"], ) 
        except:
            pass

def homepage(request):
         
    return render(request, 'base.html')


def get_word(request):
    
    if request.method == "POST":
        gotten_word = request.POST.get("word")
        #get meanings
        
        try:
            word_gotten = words.objects.get(word = gotten_word.title(), status = True)
            return render(request, 'get_word.html', {'word':word_gotten, 'gotten_word':gotten_word})
        except words.DoesNotExist:
            try:
                word_gotten = words.objects.get(word = gotten_word.upper(), status = True)
                if word_gotten:
                    return render(request, 'get_word.html', {'word':word_gotten, 'gotten_word':gotten_word})
            except words.DoesNotExist:
                try:
                    word_gotten = words.objects.get(word = gotten_word.lower(), status = True)
                    if word_gotten:
                        return render(request, 'get_word.html', {'word':word_gotten, 'gotten_word':gotten_word})
                except words.DoesNotExist:
                    suggested_word = get_close_matches(gotten_word.title(), [i.word for i in words.objects.all()])[0]
                    return render(request, 'get_word.html', {'suggested_word':suggested_word, 'gotten_word':gotten_word})
    return render(request, 'base.html')

def suggested_word_meaning(request, gotten_word):
    #get meanings
    try:
        word_gotten = words.objects.get(word = gotten_word.title(), status = True)
        return render(request, 'get_word.html', {'word':word_gotten, 'gotten_word':gotten_word})
    except words.DoesNotExist:
        word_gotten = words.objects.get(word = gotten_word.upper(), status = True)
        if word_gotten:
            return render(request, 'get_word.html', {'word':word_gotten, 'gotten_word':gotten_word})
        else:
            suggested_word = get_close_matches(gotten_word.title(), [i.word for i in words.objects.all()])[0]
            return render(request, 'get_word.html', {'suggested_word':suggested_word, 'gotten_word':gotten_word})
    
def new_word(request):
    if request.method == 'POST':
        example_3 = request.POST.get('example_3')
        example_4 = request.POST.get('example_4')
        example_5 = request.POST.get('example_5')
        form = WordForm(request.POST)
        save_form = form.save(commit = False)
        save_form.status = False
        if example_3:
            save_form.example_3 = example_3
        if example_4:
            save_form.example_4 = example_4
        if example_5:
            save_form.example_5 = example_5
        save_form.save()
        return redirect('homepage')
    return render(request, 'new_word.html')


def confirm_word(request, pk=None):
    if request.method == 'POST' and pk != None:
        word = words.objects.get(pk = pk, status = False)
        word.status = True
        word.save()
    
    words_to_confirm = words.objects.filter(status = False)
    return render(request, 'confirm_list.html', {'words':words_to_confirm})

def clear(request):
    #words_db = words.objects.all().order_by('-pk')[:6000]
    words_db = words.objects.filter(id__in=list(words.objects.values_list('pk', flat=True).order_by('-pk')[:6000])).delete()
    #words_db.delete()
    return render(request, 'base.html')

def space(request):
    for i in words.objects.all():
        i_name = i.word.rstrip()
        i.word = i_name
        i.save()
    return render(request, 'base.html')
