from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import CreateTaskForm, CreateProjectForm, CreateWorkerForm, CreateScheduleForm
from datetime import timedelta
from django.db.models import Sum

# Create your views here.


def gantt(request):
    agenda = Agenda.objects.all()
    context = {'agenda': agenda}
    return render(request, 'bridges_app/gantt.html', context)

def tarefas(request):
    tarefas = Tarefas.objects.all().order_by('-id_tar')
    total_tarefas = tarefas.count()
    projetos = Projetos.objects.all()
    create_form = CreateTaskForm(request.POST or None)

    if create_form.is_valid():
        create_form.save()
        return redirect('/tarefas')

    context = {'tarefas': tarefas, 'total_tarefas': total_tarefas, 'projetos': projetos, 'create_form': create_form}
    return render(request, 'bridges_app/tarefas.html', context)


def update_task(request, pk):
    task = Tarefas.objects.get(id_tar=pk)
    create_form = CreateTaskForm(instance=task)

    if request.method == "POST":
        create_form = CreateTaskForm(request.POST, instance=task)
        if create_form.is_valid():
            create_form.save()
            return redirect('/tarefas')

    context = {'create_form': create_form}
    return render(request, 'bridges_app/update_tarefa.html', context)


def delete_task(request, pk):
    task = Tarefas.objects.get(id_tar=pk)

    if request.method == "POST":
        task.delete()
        return redirect('/tarefas')

    context = {'task': task}
    return render(request, 'bridges_app/delete_tarefa.html', context)


def projetos(request):
    '''projetos = Projetos.objects.all()
    total_projetos = projetos.count()
    horas_projeto = projetos.objects.aggregate(total_hours=Sum('price'))
    '''
    projetos = Projetos.objects.raw('SELECT m.id_pro, m.nom_pro, '
                                    'sum(n.dur_tar_hours) + (sum(dur_tar_min) DIV 60) as total_hours, '
                                    'MOD(sum(dur_tar_min), 60) as total_minutes '
                                    'FROM bridges_app_projetos m '
                                    'LEFT JOIN bridges_app_tarefas n on  m.id_pro =  n.fk_pro_id GROUP by m.id_pro')
    total_projetos = Projetos.objects.all().count()
    create_form = CreateProjectForm(request.POST or None)

    if create_form.is_valid():
        create_form.save()
        return redirect('/projetos')

    context = {'projetos': projetos, 'create_form': create_form, 'total_projetos': total_projetos}
    return render(request, 'bridges_app/projetos.html', context)


def update_project(request, pk):
    project = Projetos.objects.get(id_pro=pk)
    create_form = CreateProjectForm(instance=project)

    if request.method == "POST":
        create_form = CreateProjectForm(request.POST, instance=project)
        if create_form.is_valid():
            create_form.save()
            return redirect('/projetos')

    context = {'create_form': create_form}
    return render(request, 'bridges_app/update_projeto.html', context)


def delete_project(request, pk):
    project = Projetos.objects.get(id_pro=pk)

    if request.method == "POST":
        project.delete()
        return redirect('/projetos')

    context = {'project': project}
    return render(request, 'bridges_app/delete_projeto.html', context)


def funcionarios(request):
    funcionarios = Funcionarios.objects.all().order_by('-id_fun')
    total_funcionarios = funcionarios.count()

    create_form = CreateWorkerForm(request.POST or None)
    if create_form.is_valid():
        create_form.save()
        return redirect('/funcionarios')

    context = {'funcionarios': funcionarios, 'total_funcionarios': total_funcionarios, 'create_form': create_form}
    return render(request, 'bridges_app/funcionarios.html', context)

def update_worker(request, pk):
    worker = Funcionarios.objects.get(id_fun=pk)
    create_form = CreateWorkerForm(instance=worker)

    if request.method == "POST":
        create_form = CreateWorkerForm(request.POST, instance=worker)
        if create_form.is_valid():
            create_form.save()
            return redirect('/funcionarios')

    context = {'create_form': create_form}
    return render(request, 'bridges_app/update_funcionario.html', context)

def delete_worker(request, pk):
    worker = Funcionarios.objects.get(id_fun=pk)

    if request.method == "POST":
        worker.delete()
        return redirect('/funcionarios')

    context = {'worker': worker}
    return render(request, 'bridges_app/delete_funcionario.html', context)

def agenda(request):
    schedules = Agenda.objects.all().order_by('-fk_tar')
    total_schedules = schedules.count()
    funcionarios = Funcionarios.objects.all()
    create_form = CreateScheduleForm(request.POST or None)

    if create_form.is_valid():
        create_form = create_form.save(commit=False)
        # aqui é onde deve vir a FORMULA MAGICA para calcular os dias
        # horas_funcionario = Funcionarios.objects.filter(create_form.fk_fun)
        # dias_semana_funcionario = Funcionarios.objects.filter(create_form.fk_fun)
        # duracao_tarefa = Tarefas.objects.filter(create_form.fk_tar)
        # if SABADO ou DOMINGO não somar
        create_form.dt_fim = create_form.dt_inicio + timedelta(days=1)
        create_form.save()
        return redirect('/agenda')

    context = {'schedules': schedules, 'total_schedules': total_schedules, 'funcionarios': funcionarios, 'create_form': create_form}
    return render(request, 'bridges_app/agenda.html', context)