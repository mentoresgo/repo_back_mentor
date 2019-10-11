from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Usuario, Roles, Valoracion, Curso, CategoriaCurso, CursoContenido, Reserva, Venta ,DetalleVenta 
from .serializers import UsuarioSerializer, RolesSerializer, ValoracionSerializer, CursoSerializer, CategoriaCursoSerializer, CursoContenidoSerializer, ReservaSerializer, VentaSerializer, DetalleVentaSerializer
# Create your views here.


class RolesView(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer


    
class UsuarioView(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ValoracionView(viewsets.ModelViewSet):
    
    queryset = Valoracion.objects.all()
    serializer_class = ValoracionSerializer

class CursoView(viewsets.ModelViewSet):
    
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class CategoriaCursoView(viewsets.ModelViewSet):
    
    queryset = CategoriaCurso.objects.all()
    serializer_class = CategoriaCursoSerializer

class CursoContenidoView(viewsets.ModelViewSet):
    
    queryset = CursoContenido.objects.all()
    serializer_class = CursoContenidoSerializer

class ReservaView(viewsets.ModelViewSet):
    
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class VentaView(viewsets.ModelViewSet):
        
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

class DetalleVentaView(viewsets.ModelViewSet):
    
    queryset = DetalleVenta.objects.all()
    serializer_class = DetalleVentaSerializer