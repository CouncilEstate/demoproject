from django.db import models

# Create your models here.

class Department(models.Model):
    position = models.CharField(max_length=50)

class Employees(models.Model):
    employee_ID = models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    telephone = models.DecimalField(max_digits=20, decimal_places=0)
    mobile = models.DecimalField(max_digits=20, decimal_places=0)
    emergency = models.DecimalField(max_digits=20, decimal_places=0)
    address = models.CharField(max_length=100)