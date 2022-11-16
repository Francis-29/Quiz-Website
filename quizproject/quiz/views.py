from django.shortcuts import render, redirect
from .models import Quiz
from result.models import Result

# Create your views here.
def home(request):
    quizzes = Quiz.objects.all()
    context = {'quizzes': quizzes}
    return render(request, 'quiz/home.html', context)


def quiz_info(request, pk):
    quiz = Quiz.objects.get(id=pk)
    context = {'quiz': quiz}
    return render(request, 'quiz/quiz-info.html', context)


def quiz_test(request, pk):
    quiz = Quiz.objects.get(id=pk)
    questions = quiz.get_questions()
    user = request.user
    if request.method == 'POST':
        data = request.POST
        data_ = data.dict()
        data_.pop('csrfmiddlewaretoken')
        data_.pop('submit')
        score = 0
        for val in data_.values():
            if val == 'True':
                score += 1
        Result.objects.create(quiz=quiz, user=user, score=score)
        return redirect('home-view')
    context = {'quiz': quiz, 'questions': questions}
    return render(request, 'quiz/quiz-test.html', context)
