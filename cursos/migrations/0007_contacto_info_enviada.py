# Generated by Django 3.2.6 on 2021-12-08 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0006_alter_contacto_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='info_enviada',
            field=models.BooleanField(default=False, verbose_name='Solicitud respondida'),
        ),
    ]
