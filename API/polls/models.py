from django.db import models

class Polls(models.Model):
    polls_text = models.CharField(max_length=20)
    start_date = models.DateTimeField('Начало опроса')
    end_date = models.DateTimeField('Конец опроса')

    def __str__(self):
        return self.polls_text


class Question(models.Model):
    polls = models.ForeignKey(Polls, on_delete=models.CASCADE,primary_key=True)
    question_text = models.CharField(max_length=120)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=120)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
# Create your models here.
