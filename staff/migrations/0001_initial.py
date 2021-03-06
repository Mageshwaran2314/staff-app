# Generated by Django 3.2.8 on 2021-12-29 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('manager', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'Department',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('date_of_birth', models.DateTimeField(auto_now=True, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('depart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.department')),
            ],
            options={
                'db_table': 'Employee',
            },
        ),
    ]
