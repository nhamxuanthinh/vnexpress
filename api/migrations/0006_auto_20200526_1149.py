# Generated by Django 3.0.5 on 2020-05-26 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200526_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]