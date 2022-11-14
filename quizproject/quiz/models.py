from django.db import models

# Create your models here.
CHOICES = [
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard')
]


class Quiz(models.Model):
    title = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    no_of_questions = models.IntegerField()
    duration = models.IntegerField(help_text="Duration of the quiz")
    passing = models.IntegerField(help_text="Required score to pass")
    difficulty = models.CharField(max_length=6, choices=CHOICES)

    def __str__(self):
        return f'{self.title} - {self.topic}'

    def get_questions(self):
        return self.question_set.all()

    class Meta:
        verbose_name_plural = 'Quizzes'
