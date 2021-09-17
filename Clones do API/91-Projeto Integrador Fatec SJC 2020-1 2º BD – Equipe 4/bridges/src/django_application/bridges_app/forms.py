from django import forms
from .models import *


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Tarefas
        fields = ['fk_pro', 'nom_tar', 'dur_tar_hours', 'dur_tar_min']

        widgets = {
            'fk_pro': forms.Select(attrs={'class': 'form-control'}),
            'nom_tar': forms.TextInput(attrs={'class': 'form-control'}),
            'dur_tar_hours': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'dur_tar_min': forms.TextInput(attrs={'class': 'form-control ', 'type': 'number', 'maxlength': "2", 'max': "59"}),
        }

        labels = {
            'fk_pro': 'Nome do Projeto',
            'nom_tar': 'Descrição da Tarefa',
            'dur_tar_hours': 'Duração da Tarefa (horas)',
            'dur_tar_min': 'Duração da Tarefa (minutos)',
        }


class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Projetos
        fields = ['nom_pro']

        widgets = {
            'nom_pro': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'nom_pro': 'Nome do Projeto',
        }


class CreateWorkerForm(forms.ModelForm):
    class Meta:
        model = Funcionarios
        fields = ['nom_fun', 'horas_limite', 'dias_semana']

        widgets = {
            'nom_fun': forms.TextInput(attrs={'class': 'form-control'}),
            'horas_limite': forms.TextInput(attrs={'class': 'form-control', 'type': 'time'}),
            'dias_semana': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', "min":"1", 'max': "7"}),
        }

        labels = {
            'nom_fun': 'Nome do Funcionário',
            'horas_limite': 'Limite de Horas Diário',
            'dias_semana': 'Dias trabalhados na Semana'
        }


class CreateScheduleForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ['fk_tar', 'fk_fun', 'dt_inicio']

        widgets = {
            'fk_tar': forms.Select(attrs={'class': 'form-control'}),
            'fk_fun': forms.Select(attrs={'class': 'form-control'}),
            'dt_inicio': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

        labels = {
            'fk_tar': 'Descrição da Tarefa',
            'fk_fun': 'Nome do Funcionário',
            'dt_inicio': 'Data de Inicio da Tarefa',
        }
