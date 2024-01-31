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



def selfjoins(request):
    EMO=Emp.objects.select_related('mgr').all()
    EMO=Emp.objects.select_related('mgr').filter(sal__gte=2500)
    #EMO=Emp.objects.select_related('mgr').filter(mgr__ename='KING')
    #EMO=Emp.objects.select_related('mgr').filter(mgr__deptno='20')
    EMO=Emp.objects.select_related('mgr').filter(deptno__dname='SALES')
    EMO=Emp.objects.select_related('mgr').filter(deptno__dloc='NEW YORK')
    EMO=Emp.objects.select_related('mgr').filter(mgr__ename='BLAKE')
    EMO=Emp.objects.select_related('mgr').filter(sal__lte=2000)
    EMO=Emp.objects.select_related('mgr').filter(deptno__dloc='NEW YORK')
    EMO=Emp.objects.select_related('mgr').filter(ename='SMITH')
    EMO=Emp.objects.select_related('mgr').filter(mgr__deptno=30)
    EMO=Emp.objects.select_related('mgr').filter(deptno__dloc='DALLAS')
    EMO=Emp.objects.select_related('mgr').filter(deptno__dname='SALES')
    EMO=Emp.objects.select_related('mgr').filter(hiredate_year=2024)

    



    d={'EMO':EMO}
    return render(request,'selfjoins.html',d)