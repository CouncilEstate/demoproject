from django.db import models

# Create your models here.

class Department(models.Model):
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.department

class Employees(models.Model):
    employee_ID = models.CharField(max_length=10, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    telephone = models.IntegerField(blank=True)
    mobile = models.IntegerField()
    emergency = models.IntegerField(blank=True)
    address = models.CharField(max_length=100)
    photo = models.ImageField(null=True, blank=True, upload_to='images/')
    email = models.EmailField(max_length=254, default="Work Email")

    objects = models.Manager()

class Meta:
    db_table = "employeedb"
