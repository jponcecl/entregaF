# Generated by Django 4.2.5 on 2023-10-07 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppF', '0004_alter_movie_descrip_alter_movie_fecha_est_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='fecha_est',
            field=models.DateField(verbose_name='Fecha de estreno'),
        ),
    ]