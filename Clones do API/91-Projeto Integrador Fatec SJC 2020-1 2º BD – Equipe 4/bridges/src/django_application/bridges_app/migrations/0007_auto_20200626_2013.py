# Generated by Django 3.0.6 on 2020-06-26 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bridges_app', '0006_auto_20200621_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='fk_tar',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bridges_app.Tarefas'),
        ),
    ]
