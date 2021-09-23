# Generated by Django 3.2.7 on 2021-09-23 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('descripcion', models.CharField(blank=True, max_length=50, null=True, verbose_name='Descripcion')),
            ],
            options={
                'db_table': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30, verbose_name='Titulo')),
                ('fecha_publicacion', models.DateField(verbose_name='Fecha publicacion')),
                ('portada', models.ImageField(upload_to='portadas')),
                ('visitas', models.PositiveIntegerField(verbose_name='Visitas')),
                ('autores', models.ManyToManyField(to='autor.Autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libro.categoria')),
            ],
            options={
                'db_table': 'libros',
            },
        ),
    ]
