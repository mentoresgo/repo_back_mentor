from rest_framework import serializers
from .models import Usuario, Roles, Valoracion, Curso, CategoriaCurso, CursoContenido, Reserva, Venta ,DetalleVenta 

#Serializadores permiten que los datos complejos,tales como Queryset
#Pueden ser facilmete trasmitidas en Json,XML o otros

#Un estilo Hyperlink nos permite que nuestro modelo pueda contener una
#direccion URL para poder tratarla desde un proveedor como HTTP
# class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Usuario
#         fields = ( 'id_usuario' ,'url','nombre','apellido','profesion','correo','contraseña','id_roles')

class RolesSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Roles
       fields =('id_roles','url','nombre','descripcion')

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Usuario
       fields =('id_usuario','url','nombre','apellido','profesion','correo','contraseña','foto','id_roles')

class CategoriaCursoSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = CategoriaCurso
       fields =('id_categoriaCurso','url','nombre','descripcion')

class CursoSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Curso
       fields =('id_curso','url','nombre','descripcion','objetivo','imagen','precio','id_usuario','id_categoriaCurso')

class CursoContenidoSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = CursoContenido
       fields =('id_cursoContenido','url','recursos','cursoContenido','id_curso')

class ValoracionSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Valoracion
       fields =('id_valoracion','url','escala','comentario')

class ReservaSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Reserva
       fields =('id_reserva','url','duracion','fecha_inicio','id_usuario','id_valoracion','id_curso')

class VentaSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Venta
       fields =('id_venta','url','fecha','logo','id_usuario')

class DetalleVentaSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = DetalleVenta
       fields =('id_detalleVenta','url','id_curso','id_venta')