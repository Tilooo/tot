#tot/tot/flashcards/models.py

from django.db import models
from django.urls import reverse
from django.views.generic import DetailView

# Language Set Model
class LanguageSet(models.Model):
    name = models.CharField(max_length=100)


# Flashcard Box Model
class FlashcardBox(models.Model):
    set = models.ForeignKey(LanguageSet, on_delete=models.CASCADE, related_name='boxes')
    name = models.CharField(max_length=100)


# Flashcard Model
class Flashcard(models.Model):
    box = models.ForeignKey(FlashcardBox, on_delete=models.CASCADE, related_name='flashcards')
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('flashcards:language_set_detail', kwargs={'pk': self.box.set.pk})


