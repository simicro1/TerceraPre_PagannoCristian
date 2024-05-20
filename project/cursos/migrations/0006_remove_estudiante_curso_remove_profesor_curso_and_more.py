# Generated by Django 5.0.4 on 2024-05-20 23:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0005_alter_estudiante_nombre_alter_profesor_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='curso',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='curso',
        ),
        migrations.AlterField(
            model_name='comision',
            name='curso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comisiones', to='cursos.curso'),
        ),
        migrations.AlterField(
            model_name='comision',
            name='estudiante',
            field=models.ManyToManyField(related_name='comisiones', to='cursos.estudiante'),
        ),
        migrations.AlterField(
            model_name='comision',
            name='profesor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comisiones', to='cursos.profesor'),
        ),
    ]
