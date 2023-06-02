#tot/tot/flashcards/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.LanguageSetListView.as_view(), name='language_set_list'),
    path('language-set/create/', views.LanguageSetCreateView.as_view(), name='language_set_create'),
    # Define other URLs for flashcard boxes and flashcards
]
