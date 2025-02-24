from django.shortcuts import render, redirect
# from .models import Denuncia
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
  return render(request, 'denuncias/index.html')
# @login_required
# def crear(request):
# def listas_denuncia(request):
#     productos = Producto.objects.all()
#     return render(request, 'productos/listar.html', {'productos': productos})

# def crear(request):
#     if request.method == "POST":
#         titulo = request.POST.get("titulo")
#         descripcion = request.POST.get("precio")
       
#     return render(request, "usuarios/crud.html")
