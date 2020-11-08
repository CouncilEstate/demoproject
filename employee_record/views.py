from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employees

# Create your views here.

def view_employees(request):
    context = {'view_employees': Employees.objects.all()}
    return render(request, "employee_record/view_employees.html", context)

def update_employees(request):
    if request.method == "GET":
         form = EmployeeForm()
         return render(request, "employee_record/update_employees.html", {'form':form})
    else:
         form = EmployeeForm(request.POST)    
         if form.is_valid():
             form.save()
         return redirect('/employee/list')    

def remove_employees(request):
    return