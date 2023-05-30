from django.shortcuts import render
from django.http import HttpRequest
from .models import Employe, Role, Dept
# Create your views here.


def home(request):
    emps = Employe.objects.all()
    context = {
        "emps": emps
    }

    return render(request, 'home.html', context)


def get_all_employe(request):
    emps = Employe.objects.all()
    context = {
        "emps": emps
    }

    return render(request, 'emps.html', context)
