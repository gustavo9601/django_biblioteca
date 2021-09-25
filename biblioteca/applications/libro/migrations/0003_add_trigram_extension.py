from django.contrib.postgres.operations import TrigramExtension
from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('libro', '0002_alter_libro_categoria'),
    ]

    operations = [
        TrigramExtension(),
    ]
