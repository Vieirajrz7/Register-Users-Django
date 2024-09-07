from django.shortcuts import render
from .models import User

def home(request):
    return render(request,'users/home.html')

def listUsers(request):
    # Save datas of screen for the database
    new_user = User() 
    new_user.name = request.POST.get('name')
    new_user.age = request.POST.get('age')
    
    new_user.save()
    # Show users registred
    
    users = {
        'users': User.objects.all()
    }
    
    # Return datas for list page for users
    return render(request,'users/users.html',users)