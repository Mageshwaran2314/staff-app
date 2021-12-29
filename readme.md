Admin page
```sh
python manage.py createsuperuser
username/password: admin/admin
```

| Page | URL |
| ------ | ------ |
| employee from | [http://127.0.0.1:8000/empfv/][PlDb] |
| Department list | [http://127.0.0.1:8000/dep/][PlGh] |
| Department detail | [http://127.0.0.1:8000/dep/<pk>][PlGd] |

## Django Questions : 

1. What command line interface instructions are required to create a django project called
‘company’ and application called ‘staff’?

```sh
django-admin startproject company
cd company 
python manage.py startapp staff
```

2. models.py - Please use the django ORM framework to create the tables below.
Employee table
Employee name
Department
Email
Date of birth
Picture
Department table
Department name
Manager (employee)

```sh
Employee and Department model created
```

3. admin.py - Please implement the code to allow the admin interface to be used to
manipulate the database for both the Employee and Department objects. When viewing
the Employee objects you should be able to filter by department and date of birth. When
creating/editing a Department object there should be inlines for each of the Employee
objects in the Department.

```sh
can add employee and department data via admin dashboard, department is inlined with employee
```

4. What command line interface instructions are required to be able to test the admin interface after you have completed #2 and #3 above?

```sh
python manage.py test
this will trigger the logic in tests.py file
```

5. views.py (Department) - Using generic class-based views please write the following views for the Department objects: list and detail

```sh
Listview is used to get all the department table rows
Detailview is used to get a particular row data
```

6. forms.py - Create a ModelForm class to create an Employee object only entering the Employee name and Department fields.

```sh
 ModelForm is used to create a form class
```

7. views.py (Employee) - Using a generic class-based view use the form in #6 in a create view for Employee objects. Is your models.py class for Employee compatible with the form and view?

```sh
using the FormView and ModelForm submission data will be verified and save to the table
```

8. What template files would be required for the views in #5 and #7 to work? Where would you put these files?
```sh
# 5
department_list.html
department_detail.html
# 7
employee_form.html
```

