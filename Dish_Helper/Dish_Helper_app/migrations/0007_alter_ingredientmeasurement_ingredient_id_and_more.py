# Generated by Django 4.1.7 on 2023-04-01 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dish_Helper_app', '0006_alter_meal_measurement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientmeasurement',
            name='ingredient_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Dish_Helper_app.ingredient'),
        ),
        migrations.AlterField(
            model_name='ingredientmeasurement',
            name='meal_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Dish_Helper_app.meal'),
        ),
    ]