from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, "index.html")


def rdsoproject(request):
    return HttpResponse("RDSO Project")