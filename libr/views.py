from django.shortcuts import render
from .models import *
from accounts.views import *
#from django.contrib.auth.forms import UserModel

# Create your views here.


def index(request):
    return render(request, 'index.html')

def classes(request):
    return render(request, 'classes.html')

def fetch(request):
    grp = request.POST['Group']
    sem = request.POST['Semister']
    books = items.objects.filter(Group=grp).filter(Semester=sem)


    return render(request, 'class_sub/subjects.html', {'books': books})

def upload(request):
    if request.method=='POST':
        obj = items()
        obj.Group = request.POST['up_Group']
        obj.Semester = request.POST['up_Semister']
        obj.Book_Name = request.POST['up_book']
        obj.Subject = request.POST['up_subject']
        obj.Uploaded_By =  request.user.first_name +" "+ request.user.last_name
        if len(request.FILES) != 0:
            obj.File = request.FILES['document']
            obj.Filesize = str("{:.3f}".format(len(obj.File)/1024))+' MB'
        obj.save()
    
    return render(request, 'upload.html')