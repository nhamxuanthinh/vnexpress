# Generated by Django 3.0.5 on 2020-05-26 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
