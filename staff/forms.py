from django import forms
from staff.models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('name', 'depart',)
