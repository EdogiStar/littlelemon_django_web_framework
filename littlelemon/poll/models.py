from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publication_date = models.DateTimeField("date published")
    status = models.BooleanField(default=1)

    def __str__(self):
        if self.status == True:
            return self.question_text + ' - Active'
        else:
            return self.question_text + ' - Closed'


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question_id = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.choice_text + ' - ' + str(self.votes)
