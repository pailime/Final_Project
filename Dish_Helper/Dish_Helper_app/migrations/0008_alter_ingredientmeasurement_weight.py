# Generated by Django 4.1.7 on 2023-04-01 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dish_Helper_app', '0007_alter_ingredientmeasurement_ingredient_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientmeasurement',
            name='weight',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
