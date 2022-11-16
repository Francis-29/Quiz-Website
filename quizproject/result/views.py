from django.shortcuts import render
from .models import Result


# Create your views here.
def result(request, pk):
    obj = Result.objects.get(id=pk)
    context = {'result': obj}
    return render(request, 'result/result.html', context)
