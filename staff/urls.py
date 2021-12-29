from django.urls import path
from staff import views


urlpatterns = [
    path('', views.home, name="Home"),
    path('dep/', views.DepartmentList.as_view(), name="Department-List"),
    path('dep/<int:pk>', views.DepartmentDetailView.as_view(), name="Department-DetailView"),

    # path('emp/', views.employeeCreate, name="EmployeeCreate"),
    path('empfv/', views.employeeFormView.as_view(), name="employee-FormView"),
]
