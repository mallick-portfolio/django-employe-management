from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employe, Role, Dept
# Create your views here.


def home(request):
    emps = Employe.objects.all()
    context = {
        "emps": emps
    }

    return render(request, 'home.html', context)


def addemploye(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = request.POST['phone']
        dept = int(request.POST['dept'])

        role = int(request.POST['role'])
        department = Dept.objects.get(id=dept)
        emp_role = Role.objects.get(id=role)
        new_emp = Employe(first_name=first_name, last_name=last_name,
                          salary=salary, bonus=bonus, phone=phone, dept=department, role=emp_role, )
        new_emp.save()
        return HttpResponse("Employe added successfully")
    else:
        return render(request, 'add_emp.html')


def deleteEmp(request, id):
    emp = Employe.objects.filter(id=id).first()
    emp.delete()
    return redirect('/')
    # return HttpResponse("Employee Removed Successfully")
