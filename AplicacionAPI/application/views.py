from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'application/home.html')

def peticiones(request):
    return render(request, 'application/peticiones.html')

def informacion(request):
    return render(request, 'application/informacion.html')