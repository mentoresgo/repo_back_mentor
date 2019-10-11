from django.contrib import admin
from .models import Usuario, Roles, Valoracion, Curso, CategoriaCurso, CursoContenido, Reserva, Venta ,DetalleVenta
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Roles)
admin.site.register(Valoracion)
admin.site.register(Curso)
admin.site.register(CategoriaCurso)
admin.site.register(CursoContenido)
admin.site.register(Reserva)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
