# Generated by Django 4.1.7 on 2023-04-08 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dish_Helper_app', '0009_rename_type_typeofmeal_meal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='calories',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
