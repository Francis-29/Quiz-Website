from django.db import models
from quiz.models import Quiz


# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=255)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    def get_answer(self):
        return self.answer_set.all()


class Answer(models.Model):
    text = models.CharField(max_length=100)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f'Question: {self.question.text} - Answer: {self.text}, {self.correct}'
