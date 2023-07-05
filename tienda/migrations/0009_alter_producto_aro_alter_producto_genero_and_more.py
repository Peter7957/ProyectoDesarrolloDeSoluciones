# Generated by Django 4.2 on 2023-07-05 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0008_alter_aro_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='aro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tienda.aro'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='genero',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tienda.genero'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='marca',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tienda.marca'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='modelo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tienda.modelo'),
        ),
    ]
