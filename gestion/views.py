from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("gestion/login.html")  # Redirige al dashboard si el login es exitoso
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
    
    return render(request, "gestion/login.html")


def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect("gestion/login.html")  # Si no está autenticado, redirige al login
    return render(request, "gestion/dashboard.html", {"user": request.user})

def logout_view(request):
    logout(request)
    return redirect("gestion/login.html")  # Redirige al login después de cerrar sesión