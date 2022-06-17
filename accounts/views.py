from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth



# Create your views here.

def register(request):
    return render(request, 'register.html')

def login(request):
    if request.method=='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pw1 = request.POST['pw1']
        pw2 = request.POST['pw2']

        if pw1==pw2:
            user = User.objects.create_user(first_name=fname, password=pw1, last_name=lname, email=email, username=email)
            user.save()

    return render(request, 'login.html')

def login_success(request):
    if request.method=='POST':
        email = request.POST['email']
        pw1 = request.POST['pw1']
        user = auth.authenticate(username=email, password=pw1)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)

    return redirect('/')