#tot/flashcards/forms.py

from django import forms
from .models import LanguageSet, FlashcardBox, Flashcard

class LanguageSetForm(forms.ModelForm):
    class Meta:
        model = LanguageSet
        fields = ['name']

class FlashcardBoxForm(forms.ModelForm):
    class Meta:
        model = FlashcardBox
        fields = ['name']

class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['question', 'answer']
