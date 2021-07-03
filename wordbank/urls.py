from django.urls import path

from .views import homepage,get_word,suggested_word_meaning

urlpatterns = [
    path('', homepage, name = 'homepage'), 
    path('get-meaning', get_word, name = 'get-meaning'),
    path('get-meaning/<str:gotten_word>/', suggested_word_meaning, name = 'suggest')
]
