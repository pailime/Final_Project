# Generated by Django 4.1.7 on 2023-04-01 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dish_Helper_app', '0005_alter_meal_measurement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='measurement',
            field=models.ManyToManyField(through='Dish_Helper_app.IngredientMeasurement', to='Dish_Helper_app.ingredient'),
        ),
    ]
