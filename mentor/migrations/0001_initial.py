# Generated by Django 2.2.5 on 2019-10-11 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaCurso',
            fields=[
                ('id_categoriaCurso', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id_curso', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=60)),
                ('objetivo', models.CharField(max_length=120)),
                ('imagen', models.ImageField(upload_to='')),
                ('precio', models.FloatField(max_length=19.4)),
                ('id_categoriaCurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentor.CategoriaCurso')),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id_roles', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=250)),
                ('desripcion', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('profesion', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=250)),
                ('contraseña', models.CharField(max_length=50)),
                ('foto', models.ImageField(upload_to='')),
                ('id_roles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentor.Roles')),
            ],
        ),
        migrations.CreateModel(
            name='Valoracion',
            fields=[
                ('id_valoracion', models.AutoField(primary_key=True, serialize=False)),
                ('escala', models.IntegerField(max_length=11)),
                ('comentario', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField()),
                ('logo', models.ImageField(upload_to='')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentor.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id_reserva', models.AutoField(primary_key=True, serialize=False)),
                ('duracion', models.DurationField()),
                ('fecha_inicio', models.DateField()),
                ('id_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentor.Curso')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentor.Usuario')),
                ('id_valoracion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentor.Valoracion')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id_detalleVenta', models.AutoField(primary_key=True, serialize=False)),
                ('id_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentor.Curso')),
                ('id_venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentor.Venta')),
            ],
        ),
        migrations.CreateModel(
            name='CursoContenido',
            fields=[
                ('id_cursoContenido', models.AutoField(primary_key=True, serialize=False)),
                ('recursos', models.IntegerField(max_length=11)),
                ('cursoContenido', models.CharField(max_length=45)),
                ('id_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentor.Curso')),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentor.Usuario'),
        ),
    ]