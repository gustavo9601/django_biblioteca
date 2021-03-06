# Generated by Django 3.2.7 on 2021-09-25 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0002_alter_libro_categoria'),
        ('lector', '0002_alter_prestamo_lector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='lector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lector.lector'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='libro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libro_prestamo', to='libro.libro'),
        ),
    ]
