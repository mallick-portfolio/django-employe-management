from django.db import models
from datetime import datetime
# Create your models here.


class Dept(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Employe(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    salary = models.IntegerField()
    bonus = models.IntegerField()
    phone = models.CharField(max_length=11)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    hired_date = models.DateTimeField(default=datetime.now())

    def __str__(self) -> str:
        return "%s %s %s" % (self.first_name, self.last_name, self.phone)
