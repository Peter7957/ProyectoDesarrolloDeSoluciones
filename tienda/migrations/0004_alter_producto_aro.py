# Generated by Django 4.2.1 on 2023-05-11 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_aro_genero_producto_aro_producto_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='aro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tienda.aro'),
        ),
    ]