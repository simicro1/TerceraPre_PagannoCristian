# Generated by Django 5.0.4 on 2024-04-25 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0003_comision_curso_alter_comision_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comision',
            name='nombre',
            field=models.PositiveBigIntegerField(unique=True),
        ),
    ]
