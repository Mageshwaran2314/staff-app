from django.contrib import admin
from staff.models import Department, Employee


class EmployeeInline(admin.StackedInline):
    model = Employee

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name", "manager"]
    inlines = [
        EmployeeInline,
    ]

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["name", "depart", "date_of_birth"]


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
