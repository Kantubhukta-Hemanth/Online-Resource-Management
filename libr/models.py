from datetime import datetime
from email.headerregistry import Group
from django.db import models
import os

# Create your models here.

class items(models.Model):
    Subject = models.TextField()
    Book_Name = models.TextField()
    Group = models.TextField(max_length=30)
    Semester = models.TextField()
    Uploaded_By = models.TextField()
    File = models.FileField(upload_to='User_Media', null=True, blank=True)
    Filesize = models.TextField()