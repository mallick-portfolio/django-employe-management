from django.urls import path
from .views import home, addemploye, deleteEmp
urlpatterns = [
    path('', home),
    path('add-emp/', addemploye, name='add-emp'),
    path('delete-emp/<int:id>/', deleteEmp, name='delete-emp')
]
