from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def signup(request):
    if request.method=="POST":
        username = request.POST['username']
        firstame = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email_id']
        password = request.POST['password']    
        
        x = User.objects.create_user(username=username, first_name=firstame, last_name=lastname,email=email, password=password)
        print('user created')

        return redirect('/')  
    
    else:
        return render(request,'signup.html')
    

# Create your views here.
