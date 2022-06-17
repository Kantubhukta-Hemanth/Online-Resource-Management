from unicodedata import name
from xml.dom.minidom import Document
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('classes/', views.classes, name='classes'),
    path('classes/fetch', views.fetch, name='fetch'),
    path('upload/', views.upload, name = 'add-item')
] #+ static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)