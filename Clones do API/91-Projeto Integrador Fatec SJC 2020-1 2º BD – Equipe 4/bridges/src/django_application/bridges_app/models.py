from django.db import models

# Create your models here.


class Projetos(models.Model):
    id_pro = models.AutoField(primary_key=True)
    nom_pro = models.CharField(max_length=200)

    def __str__(self):
        return self.nom_pro


class Tarefas(models.Model):
    id_tar = models.AutoField(primary_key=True)
    fk_pro = models.ForeignKey(Projetos, on_delete=models.CASCADE)
    nom_tar = models.CharField(max_length=200)
    dur_tar_hours = models.DecimalField(max_digits=5, decimal_places=2)
    dur_tar_min = models.DecimalField(max_digits=4, decimal_places=2)


    def __str__(self):
        return self.nom_tar


class Funcionarios(models.Model):
    id_fun = models.AutoField(primary_key=True)
    nom_fun = models.CharField(max_length=200)
    horas_limite = models.TimeField()
    dias_semana = models.IntegerField()

    def __str__(self):
        return self.nom_fun


class Agenda(models.Model):
    fk_tar = models.OneToOneField(Tarefas, on_delete=models.CASCADE)
    fk_fun = models.ForeignKey(Funcionarios, on_delete=models.CASCADE)
    dt_inicio = models.DateField()
    dt_fim = models.DateField()