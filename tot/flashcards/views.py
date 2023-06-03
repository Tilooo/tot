from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.template.loader import get_template
from django.http import HttpResponseServerError
from .models import LanguageSet, FlashcardBox, Flashcard
from .forms import LanguageSetForm, FlashcardBoxForm, FlashcardForm


def clear_template_cache(request):
    try:
        get_template('base.html').template.cache.clear()
    except Exception as e:
        return HttpResponseServerError(f"Error clearing template cache: {str(e)}")


# Language Set Views
class LanguageSetListView(ListView):
    model = LanguageSet
    template_name = 'flashcards/language_set_list.html'
    context_object_name = 'language_sets'


class LanguageSetCreateView(CreateView):
    model = LanguageSet
    template_name = 'flashcards/language_set_form.html'
    form_class = LanguageSetForm
    success_url = reverse_lazy('flashcards:language_set_list')


class LanguageSetUpdateView(UpdateView):
    model = LanguageSet
    template_name = 'flashcards/language_set_form.html'
    form_class = LanguageSetForm
    success_url = reverse_lazy('flashcards:language_set_list')


class LanguageSetDeleteView(DeleteView):
    model = LanguageSet
    template_name = 'flashcards/language_set_confirm_delete.html'
    success_url = reverse_lazy('flashcards:language_set_list')


class LanguageSetDetailView(DetailView):
    model = LanguageSet
    template_name = 'flashcards/language_set_detail.html'
    context_object_name = 'language_set'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['boxes'] = FlashcardBox.objects.filter(language_set=self.object)
        return context


# Flashcard Box Views

class FlashcardBoxCreateView(CreateView):
    model = FlashcardBox
    template_name = 'flashcards/box_form.html'
    form_class = FlashcardBoxForm


class FlashcardBoxDeleteView(DeleteView):
    model = FlashcardBox
    template_name = 'flashcards/box_confirm_delete.html'


    def get_success_url(self):
        return reverse_lazy('flashcards:language_set_detail', kwargs={'pk': self.object.set.pk})


class FlashcardBoxDetailView(DetailView):
    model = FlashcardBox
    template_name = 'flashcards/box_detail.html'
    context_object_name = 'flashcard_box'


# Flashcard Views

class FlashcardCreateView(CreateView):
    model = Flashcard
    template_name = 'flashcards/flashcard_create.html'
    form_class = FlashcardForm


class FlashcardUpdateView(UpdateView):
    model = Flashcard
    template_name = 'flashcards/flashcard_update.html'
    form_class = FlashcardForm


class FlashcardDeleteView(DeleteView):
    model = Flashcard
    template_name = 'flashcards/flashcard_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('flashcards:box_detail', kwargs={'pk': self.object.box.pk})
