from django.shortcuts import render
from .forms import EmployeeForm

# Create your views here.

def view_employees(request):
    return render(request, "employee_record/view_employees.html")

def update_employees(request):
    form = EmployeeForm()
    return render(request, "employee_record/update_employees.html", {'form':form})

def remove_employees(request):
    return