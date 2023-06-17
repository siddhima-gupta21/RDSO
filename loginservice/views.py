from django.shortcuts import redirect, render
from django.contrib import auth

# Create your views here.

def login(request):
    if request.method=='POST':
        usernamex=request.POST['username']
        passwordx=request.POST['password']
        
        x=auth.authenticate(username=usernamex,password=passwordx)
        
        if x is None:
            return redirect('login')
        else:
            return redirect('database')
            
    else:
        return render(request,'login.html')
