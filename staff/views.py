from django.shortcuts import render
from django.http import HttpResponse
from staff.models import Department, Employee
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from staff.forms import EmployeeForm


def home(request):
    return HttpResponse("<h1>Hello</h1>")


class DepartmentList(ListView):
    template_name = 'department_list.html'
    model = Department


class DepartmentDetailView(DetailView):
    template_name = 'department_detail.html'
    model = Department


# def employeeCreate(request):
#     # initate a new form
#     form = EmployeeForm()
#     context = {'form': form}
#     if request.method == "POST":
#         form = EmployeeForm(request.POST)
#         if form.is_valid(): # validate and save
#             # save the incoming data in models
#             form.save()
#     return render(request, 'employee_form.html', context)


class employeeFormView(FormView):
    form_class = EmployeeForm
    template_name = "employee_form.html"
    success_url ="/empfv/" # success redirection url
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
