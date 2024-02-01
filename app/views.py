from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models import Q



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





def emp_mgr_dept(request):
    EMD=Emp.objects.select_related('deptno','mgr').all()
    EMD=Emp.objects.select_related('deptno','mgr').filter(ename='SMITH')
    EMD=Emp.objects.select_related('deptno','mgr').filter(sal__gte=2500)
    EMD=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='KING')
    EMD=Emp.objects.select_related('deptno','mgr').filter(mgr__deptno='20')
    EMD=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='SALES')
    EMD=Emp.objects.select_related('deptno','mgr').filter(deptno__dloc='NEW YORK')
    EMD=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='BLAKE')
    EMD=Emp.objects.select_related('deptno','mgr').filter(sal__lte=2000)
    EMD=Emp.objects.select_related('deptno','mgr').filter(deptno__dloc='NEW YORK')
    EMD=Emp.objects.select_related('deptno','mgr').filter(ename='SMITH')
    EMD=Emp.objects.select_related('deptno','mgr').filter(mgr__deptno=30)
    EMD=Emp.objects.select_related('deptno','mgr').filter(deptno__dloc='DALLAS')
    EMD=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='SALES')
    EMD=Emp.objects.select_related('deptno','mgr').filter(ename__startswith='A')
    EMD=Emp.objects.select_related('deptno','mgr').filter(ename='SMITH',sal__lte=1000)
    EMD=Emp.objects.select_related('deptno','mgr').filter(Q(hiredate__year=2024) |Q(ename__startswith='A'))
    EMD=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='RESEARCH')
    


                                
    d={'EMD':EMD}
    return render(request,'emp_mgr_dept.html',d)