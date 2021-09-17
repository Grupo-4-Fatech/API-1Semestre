from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    return render(request, 'polls/tarefas.html')

def hello(request):
    return HttpResponse("Vamos dar as mãos 123")

def tarefas(request):
    return render(request, 'polls/tarefas.html')

def funcionarios(request):
    funcionario = Func.objects.all()
    return render(request, 'polls/funcionarios.html', {'list':funcionario})