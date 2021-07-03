from django.urls import path

from .views import homepage,get_word,suggested_word_meaning,new_word,confirm_word,create_words

urlpatterns = [
    path('create-words', create_words, name = 'create_words'),
    path('', homepage, name = 'homepage'), 
    path('get-meaning', get_word, name = 'get-meaning'),
    path('get-meaning/<str:gotten_word>/', suggested_word_meaning, name = 'suggest'),
    path("new-word", new_word, name = "new-word"),
    path("confirm-word/<int:pk>", confirm_word, name = 'confirm-words'),
    path("confirm-word", confirm_word, name = 'confirm-word'),
    
    
]
