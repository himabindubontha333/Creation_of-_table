from django.shortcuts import render
from app.models import *

# Create your views here.
def dept(request):
    LOD=Department.objects.all()
    d={'department':LOD}
    return render(request,'dept.html',context=d)
def Emp(request):
    LOE=Employe.objects.all()
    d={'employe':LOE}
    return render(request,'emp.html',context=d)
