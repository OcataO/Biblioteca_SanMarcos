# Generated by Django 4.2.7 on 2023-12-03 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appejemplares', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='libro',
            options={'verbose_name': 'Datos_Libros'},
        ),
        migrations.AlterField(
            model_name='libro',
            name='categoria',
            field=models.CharField(choices=[('novelas', 'Novelas'), ('suspenso', 'Suspenso'), ('historia', 'Historia'), ('test', 'Test')], max_length=50, verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='ubicacion',
            field=models.CharField(max_length=20, verbose_name='Ubicación'),
        ),
    ]
