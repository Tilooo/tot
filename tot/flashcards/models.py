#tot/tot/flashcards/models.py

from django.db import models

class LanguageSet(models.Model):
    name = models.CharField(max_length=100)

class FlashcardBox(models.Model):
    set = models.ForeignKey(LanguageSet, on_delete=models.CASCADE, related_name='boxes')
    name = models.CharField(max_length=100)

class Flashcard(models.Model):
    box = models.ForeignKey(FlashcardBox, on_delete=models.CASCADE, related_name='flashcards')
    question = models.TextField()
    answer = models.TextField()
