#tot/flashcards/urls.py

from django.urls import path
from . import views

app_name = 'flashcards'

urlpatterns = [
    path('', views.LanguageSetListView.as_view(), name='language_set_list'),
    path('language-set/create/', views.LanguageSetCreateView.as_view(), name='language_set_create'),
    path('language-set/update/<int:pk>/', views.LanguageSetUpdateView.as_view(), name='language_set_update'),
    path('language-set/delete/<int:pk>/', views.LanguageSetDeleteView.as_view(), name='language_set_delete'),
    path('language-set/detail/<int:pk>/', views.LanguageSetDetailView.as_view(), name='language_set_detail'),
    path('flashcard-box/create/', views.FlashcardBoxCreateView.as_view(), name='box_create'),
    path('flashcard-box/update/<int:pk>/', views.FlashcardBoxCreateView.as_view(), name='box_update'),
    path('flashcard-box/delete/<int:pk>/', views.FlashcardBoxDeleteView.as_view(), name='box_delete'),
    path('flashcard/create/', views.FlashcardCreateView.as_view(), name='flashcard_create'),
    path('flashcard/update/<int:pk>/', views.FlashcardUpdateView.as_view(), name='flashcard_update'),
    path('flashcard/delete/<int:pk>/', views.FlashcardDeleteView.as_view(), name='flashcard_delete'),
]







