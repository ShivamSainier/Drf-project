# Generated by Django 3.2 on 2021-08-19 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quantity',
            name='amount',
            field=models.IntegerField(blank=True),
        ),
    ]