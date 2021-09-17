from django.db import models

# Create your models here.

class Func(models.Model):
    name = models.CharField(max_length=200, null=True)
    total_hours = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
