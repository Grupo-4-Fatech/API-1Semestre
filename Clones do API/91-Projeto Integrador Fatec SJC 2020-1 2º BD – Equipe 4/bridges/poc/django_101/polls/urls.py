from django.urls import path
from . import views

urlpatterns = [
    path('tarefas', views.tarefas, name='tela tarefas'),
    path('hello', views.hello, name='565'),
    path('funcionarios', views.funcionarios, name='tela de funcionarios'),
]