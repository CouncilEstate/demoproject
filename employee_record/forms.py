from django import forms
from .models import Employees

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employees
        fields = '__all__'
        labels = {
            'firstname': 'First Name',
            'lastname': 'Last Name',
            'emergency': 'Emergency Contact',
            'photo': 'Employee Photo',
            'email': 'Email'
        }

      