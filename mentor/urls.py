from django.urls import path, include
from .import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('roles',views.RolesView)
router.register('usuario',views.UsuarioView)
router.register('valoracion',views.ValoracionView)
router.register('curso',views.CursoView)
router.register('categoriaCurso',views.CategoriaCursoView)
router.register('cursoContenido',views.CursoContenidoView) 
router.register('reserva',views.ReservaView) 
router.register('venta',views.VentaView)     
router.register('detalleventa',views.DetalleVentaView)     


urlpatterns = [
    path('',include(router.urls)),
]
