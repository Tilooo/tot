#tot/tot/flashcards/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import LanguageSet, FlashcardBox, Flashcard

# Language Set Views

class LanguageSetListView(ListView):
    model = LanguageSet
    template_name = 'flashcards/language_set_list.html'
    context_object_name = 'language_sets'

class LanguageSetCreateView(CreateView):
    model = LanguageSet
    template_name = 'flashcards/language_set_form.html'
    fields = ['name']

class LanguageSetUpdateView(UpdateView):
    model = LanguageSet
    template_name = 'flashcards/language_set_form.html'
    fields = ['name']

class LanguageSetDeleteView(DeleteView):
    model = LanguageSet
    template_name = 'flashcards/language_set_confirm_delete.html'
    success_url = reverse_lazy('flashcards:language_set_list')

# Flashcard Box Views

class FlashcardBoxCreateView(CreateView):
    model = FlashcardBox
    template_name = 'flashcards/flashcard_box_form.html'
    fields = ['set', 'name']

class FlashcardBoxUpdateView(UpdateView):
    model = FlashcardBox
    template_name = 'flashcards/flashcard_box_form.html'
    fields = ['set', 'name']

class FlashcardBoxDeleteView(DeleteView):
    model = FlashcardBox
    template_name = 'flashcards/flashcard_box_confirm_delete.html'
    context_object_name = 'box'

    def get_success_url(self):
        return reverse_lazy('flashcards:language_set_detail', kwargs={'pk': self.object.set.pk})

# Flashcard Views

class FlashcardCreateView(CreateView):
    model = Flashcard
    template_name = 'flashcards/flashcard_form.html'
    fields = ['box', 'question', 'answer']

class FlashcardUpdateView(UpdateView):
    model = Flashcard
    template_name = 'flashcards/flashcard_form.html'
    fields = ['box', 'question', 'answer']

class FlashcardDeleteView(DeleteView):
    model = Flashcard
    template_name = 'flashcards/flashcard_confirm_delete.html'
    context_object_name = 'flashcard'

    def get_success_url(self):
        return reverse_lazy('flashcards:flashcard_box_detail', kwargs={'pk': self.object.box.pk})
