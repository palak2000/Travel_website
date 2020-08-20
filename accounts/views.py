from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

from . import views
from .models import Contact


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials. Please Try Again.')
            return redirect('login')
    else:
        return render(request, 'login.html')


# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Is Already Present. Try Using Another Username.')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Is Already Present. Try Using Another Email.')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name,
                                                last_name=last_name)
                user.save();
                # messages.info(request, 'User Created')
                return redirect('login')

        else:
            messages.info(request, 'Password Donot match.Try Again.')
            return redirect('register')
        return redirect('/')

    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def contact(request):
    pass
    if request.method == 'POST':
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')

        c = Contact(email=email_r, subject=subject_r, message=message_r)
        c.save()

        return redirect('/')
    else:
        return render(request, 'contact.html')


def Mumbai(request):
    # dests = Destination.objects.all()

    return render(request, 'mumbai.html')


def Bhopal(request):
    # dests = Destination.objects.all()

    return render(request, 'Bhopal.html')


def Jaipur(request):
    # dests = Destination.objects.all()

    return render(request, 'Jaipur.html')


'''def Hyderabad(request):
    # dests = Destination.objects.all()

    return render(request, 'Hyderabad.html')
'''


def Pune(request):
    # dests = Destination.objects.all()

    return render(request, 'Pune.html')
