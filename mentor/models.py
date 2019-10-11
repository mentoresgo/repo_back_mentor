from django.db import models

class Roles(models.Model):
    id_roles = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250, blank=False, null=False)
    descripcion = models.TextField(null=True)

    class Meta:
        verbose_name ="Rol"
        verbose_name_plural ="Roles"
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre 

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False) 
    apellido = models.CharField(max_length=50, blank=False, null=False)
    profesion = models.CharField(max_length=100, blank=False, null=False)
    correo = models.EmailField(max_length=250)
    contraseña = models.CharField(max_length=50)
    foto = models.ImageField()
    id_roles = models.ForeignKey(Roles, on_delete = models.CASCADE)

    class Meta:
        verbose_name ="Usuario"
        verbose_name_plural ="Usuario"
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre 

class CategoriaCurso(models.Model):
    id_categoriaCurso = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=False, null=False)
    descripcion = models.TextField(null=True)

    class Meta:
        verbose_name ="CategoriaCurso"
        verbose_name_plural ="CategoriaCursos"
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre 

class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=False, null=False)
    descripcion = models.CharField(max_length=60, blank=False, null=False)
    objetivo = models.CharField(max_length=120, blank=False, null=False)
    imagen = models.ImageField()
    precio = models.FloatField(max_length=19.4)
    id_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    id_categoriaCurso = models.ForeignKey(CategoriaCurso,on_delete=models.CASCADE)

    class Meta:
        verbose_name ="Curso"
        verbose_name_plural ="Cursos"
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre 

class CursoContenido(models.Model):
    id_cursoContenido = models.AutoField(primary_key=True)
    recursos = models.IntegerField()
    cursoContenido = models.CharField(max_length=45, blank=False, null=False)
    id_curso = models.ForeignKey(Curso,on_delete=models.CASCADE)

class Valoracion(models.Model):
    id_valoracion = models.AutoField(primary_key=True)
    escala = models.IntegerField()
    comentario = models.CharField(max_length=120)

class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    duracion = models.DurationField(blank=False, null=False)
    fecha_inicio = models.DateField()
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_valoracion = models.ForeignKey(Valoracion,on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
     
class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    fecha = models.DateTimeField()
    logo = models.ImageField()
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class DetalleVenta(models.Model):
    id_detalleVenta = models.AutoField(primary_key=True)
    id_curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    id_venta = models.ForeignKey(Venta,on_delete=models.CASCADE)







# Create your models here.
