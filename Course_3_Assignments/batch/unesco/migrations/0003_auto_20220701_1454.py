# Generated by Django 3.2.5 on 2022-07-01 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0002_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(default='', max_length=500),
        ),
    ]