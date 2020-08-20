from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('contact', views.contact, name='contact'),
    path('Mumbai', views.Mumbai, name='Mumbai'),
    path('Bhopal', views.Bhopal, name='Bhopal'),
    path('Jaipur', views.Jaipur, name='Jaipur'),
    # path('Hyderabad', views.Hyderabad, name='Hyderabad'),
    path('Pune', views.Pune, name='Pune')
]
