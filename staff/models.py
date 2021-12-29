from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=True, null=True)
    manager = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        db_table = "Department"

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    depart = models.ForeignKey(Department, on_delete = models.CASCADE) # mentioned as depart due to conflict in migration
    email = models.CharField(max_length=100, unique=True, blank=True, null=True)
    date_of_birth = models.DateTimeField(auto_now=True, blank=True, null=True)
    picture = models.ImageField(upload_to ='uploads/', blank=True, null=True)
    
    class Meta:
        db_table = "Employee"

    def __str__(self):
        return self.name





