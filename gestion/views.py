from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from gestion.forms import DocenteForm

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

def agregar_docente(request):
    if request.method == 'POST':
        form = DocenteForm(request.POST, request.FILES)  # Incluye request.FILES para manejar archivos
        if form.is_valid():
            form.save()
            return redirect('lista_docentes')  # Redirige a la página de lista de docentes
    else:
        form = DocenteForm()
    return render(request, 'agregar_docente.html', {'form': form})

def lista_docentes(request):
    docentes = docentes.objects.all()  # Obtiene todos los docentes de la base de datos
    return render(request, 'lista_docentes.html', {'docentes': docentes})
