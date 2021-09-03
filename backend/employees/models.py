from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=500)
    department = models.CharField(max_length=500)
    date_of_joining = models.DateField()

    def __str__(self) -> str:
        return self.name
