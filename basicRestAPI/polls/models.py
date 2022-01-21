import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # para devolver el texto en vez del objeto de tipo Question al
    def __str__(self):
        return self.question_text

    # custom method get the recently question asked
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # campo relacional depende de question_text
    choice_text = models.CharField(max_length=200)  # los campos de tipo CharField requieren definir un max_length
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
