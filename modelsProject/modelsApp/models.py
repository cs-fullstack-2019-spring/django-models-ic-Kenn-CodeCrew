from django.db import models

# Create your models here.
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

# name, stars, and releaseDate
class Movie(models.Model):
    name = models.CharField(max_length=150)
    starRating = models.DecimalField(decimal_places=1, max_digits=3)
    releaseDate = models.DateField()