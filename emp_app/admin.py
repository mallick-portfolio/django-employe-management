from django.contrib import admin
from .models import Dept, Role, Employe
# Register your models here.


admin.site.register(Employe)
admin.site.register(Role)
admin.site.register(Dept)