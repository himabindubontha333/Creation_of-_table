from django.db import models

# Create your models here.
class Department(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    Loc=models.CharField(max_length=100)
class Employe(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    MGR=models.CharField(max_length=100)
    hiredate=models.DateField()
    sal=models.IntegerField()
    comm=models.IntegerField(blank=True)
    deptno=models.IntegerField()
