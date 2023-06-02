#tot/tot/flashcards/urls.py

from django.urls import path
from .views import (
    LanguageSetListView, LanguageSetCreateView, LanguageSetUpdateView, LanguageSetDeleteView,
    FlashcardBoxCreateView, FlashcardBoxUpdateView, FlashcardBoxDeleteView,
    FlashcardCreateView, FlashcardUpdateView, FlashcardDeleteView
)

app_name = 'flashcards'

urlpatterns = [
    path('', LanguageSetListView.as_view(), name='language_set_list'),
    path('language-set/create/', LanguageSetCreateView.as_view(), name='language_set_create'),
    path('language-set/update/<int:pk>/', LanguageSetUpdateView.as_view(), name='language_set_update'),
    path('language-set/delete/<int:pk>/', LanguageSetDeleteView.as_view(), name='language_set_delete'),
    path('flashcard-box/create/', FlashcardBoxCreateView.as_view(), name='flashcard_box_create'),
    path('flashcard-box/update/<int:pk>/', FlashcardBoxUpdateView.as_view(), name='flashcard_box_update'),
    path('flashcard-box/delete/<int:pk>/', FlashcardBoxDeleteView.as_view(), name='flashcard_box_delete'),
    path('flashcard/create/', FlashcardCreateView.as_view(), name='flashcard_create'),
    path('flashcard/update/<int:pk>/', FlashcardUpdateView.as_view(), name='flashcard_update'),
    path('flashcard/delete/<int:pk>/', FlashcardDeleteView.as_view(), name='flashcard_delete'),
]


