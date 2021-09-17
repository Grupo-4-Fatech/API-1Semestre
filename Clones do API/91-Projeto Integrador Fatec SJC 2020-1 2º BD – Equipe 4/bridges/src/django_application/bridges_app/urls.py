from django.urls import path
from . import views

urlpatterns = [
    path('', views.gantt, name='gantt'),
    path('tarefas', views.tarefas, name='Tarefas'),
    path('update_task/<int:pk>', views.update_task, name='update_task'),
    path('delete_task/<int:pk>', views.delete_task, name='delete_task'),
    path('projetos', views.projetos, name='projetos'),
    path('update_project/<int:pk>', views.update_project, name='update_project'),
    path('delete_project/<int:pk>', views.delete_project, name='delete_project'),
    path('funcionarios', views.funcionarios, name='funcionarios'),
    path('update_worker/<int:pk>', views.update_worker, name='update_worker'),
    path('delete_worker/<int:pk>', views.delete_worker, name='delete_worker'),
    path('agenda', views.agenda, name='agenda'),
]