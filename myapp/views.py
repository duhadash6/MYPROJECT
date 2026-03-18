from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .models import Feature

def index(request):
    features = Feature.objects.all()
    return render(request, 'myapp/index.html', {'features': features})

def counter(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        amount_of_words = len(text.split())
        return render(request, 'myapp/counter.html', {'amount': amount_of_words, 'text': text})

    return render(request, 'myapp/counter.html', {'amount': None, 'text': ''})
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email existe deja')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username existe deja')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'MDP non identiques')
            return redirect('register')
    else:
        return render(request, 'myapp/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Cred invalid')
    return render(request, 'myapp/login.html')



def logout(request):
    auth.logout(request)
    return redirect('index')
