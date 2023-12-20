from django.db import models

# Create your models here.

class Add_task(models.Model):
    task = models.CharField(max_length=50)
    priority = models.CharField(max_length=2)
    date = models.DateField()

    def __str__(self):
        return self.task