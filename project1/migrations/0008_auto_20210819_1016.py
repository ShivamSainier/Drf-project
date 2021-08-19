# Generated by Django 3.2 on 2021-08-19 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0007_alter_products_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_details',
            name='products',
        ),
        migrations.AddField(
            model_name='user_details',
            name='products',
            field=models.ManyToManyField(to='project1.Products'),
        ),
    ]
