# Generated by Django 4.1.7 on 2023-04-01 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dish_Helper_app', '0003_rename_user_profile_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredientmeasurement',
            name='meal_id',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='Dish_Helper_app.meal'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='meal',
            name='measurement',
        ),
        migrations.AddField(
            model_name='meal',
            name='measurement',
            field=models.ManyToManyField(through='Dish_Helper_app.IngredientMeasurement', to='Dish_Helper_app.ingredient'),
        ),
    ]