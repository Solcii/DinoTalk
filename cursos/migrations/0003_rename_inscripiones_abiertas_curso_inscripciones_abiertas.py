# Generated by Django 3.2.6 on 2021-12-01 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_auto_20211201_2031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='inscripiones_abiertas',
            new_name='inscripciones_abiertas',
        ),
    ]