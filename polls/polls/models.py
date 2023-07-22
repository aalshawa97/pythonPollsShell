from django.utils import timezone
from django.db import models
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - self.pub_date < timezone.timedelta(days=7)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.CharField(max_length=200, default="Default Question Text")
    choice_text = models.CharField(max_length=200, default="Default Choice Text")
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
