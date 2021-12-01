# Generated by Django 3.2.6 on 2021-12-01 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profesor',
            options={'verbose_name': 'Profesor', 'verbose_name_plural': 'Profesores'},
        ),
        migrations.AddField(
            model_name='curso',
            name='inscripiones_abiertas',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='duracion',
            field=models.PositiveIntegerField(default=30, verbose_name='Duración (días)'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='apellido',
            field=models.CharField(max_length=50, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='dni',
            field=models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='DNI'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='fecha_nacimiento',
            field=models.DateField(verbose_name='Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
    ]
