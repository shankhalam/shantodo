from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, ("Invalid Credentials, Try Again."))
            return redirect('login')
    return render(request, 'authenticate/login.html')

def user_logout(request):
    logout(request)
    messages.success(request, ("Logged out successfully. Thank You."))
    return redirect('login')
