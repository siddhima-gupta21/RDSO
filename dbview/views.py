from django.shortcuts import render
from .models import employee
# Create your views here.

def database(request):
    all_employee = employee.objects.all
    return render(request, 'database.html', {'all': all_employee})

