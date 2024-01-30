from django.shortcuts import render

# Create your views here.
from app.models import *



def equijoins(request):
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2024)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dloc='NEW YORK')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno=10)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno=30)
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    #EMPOBJECTS=Emp.objects.select_related('deptno').all()[3:5:]
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='RESEARCH')








    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoins.html',d)

