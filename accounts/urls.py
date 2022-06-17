from django.urls import path, include


from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('login_success', views.login_success, name='login_success'),
    path('logout', views.logout, name='logout')
]