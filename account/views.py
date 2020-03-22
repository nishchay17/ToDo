from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username= username, password= password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logout(request):
    if not request.user.is_authenticated:
        return redirect('login')
    auth.logout(request)
    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password2 != password1:
            messages.info(request, 'Passwords do not match')
        elif User.objects.filter(username= username).exists():
            messages.info(request, "Username already exists")
        else:
            user = User.objects.create_user(
                username= username,
                email=email,
                password=password1,
                )
            user.save()
            return redirect("/")
        return redirect("register")

    return render(request, 'register.html')