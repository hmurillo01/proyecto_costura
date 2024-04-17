# Generated by Django 5.0.2 on 2024-04-16 00:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Costureras',
            fields=[
                ('identificacion', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=200)),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Fabrica',
            fields=[
                ('nit', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('costura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fabrica.costureras')),
            ],
        ),
        migrations.CreateModel(
            name='Tareas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('cant_prendas', models.IntegerField()),
                ('fecha_ini', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('costurera', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='fabrica.costureras')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fabrica.estado')),
                ('fabrica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fabrica.fabrica')),
            ],
        ),
    ]
