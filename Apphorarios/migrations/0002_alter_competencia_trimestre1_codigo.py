# Generated by Django 3.2.4 on 2021-12-13 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apphorarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competencia_trimestre1',
            name='codigo',
            field=models.CharField(max_length=100),
        ),
    ]
