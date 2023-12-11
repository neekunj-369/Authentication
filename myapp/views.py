from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import feature
from django.contrib.auth.models import User, auth
from django.contrib.auth import login
from django.contrib import messages


# Create your views here.


def index(request):
    features = feature.objects.all()

    return render(request, 'index.html', {'features': features})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # if password == password2:
        #     user = User.objects.create_user(username, email, password)
        #     user.save()
        #     messages.success(request, 'successfully created')
        #     return redirect('index')

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username already used')
                return redirect('register')
            else:
                user = User.objects.create_user(username, email, password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'password not same')
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def post(request, pk):
    return render(request, 'post.html', {'pk': pk})
