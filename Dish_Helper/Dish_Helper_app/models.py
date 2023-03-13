from django.db import models


class User(models.Model):
    name = models.CharField(max_length=128, null=False)
    last_name = models.CharField(max_length=256, null=False)
    email = models.EmailField(null=False)


class Meal(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()
    recipe = models.TextField()
    total_time = models.PositiveIntegerField()
    # servings = models.PositiveSmallIntegerField()
    ingredients = models.ManyToManyField('Ingredient')


class TypeOfMeal(models.Model):

    CHOICES = [
        (0, 'breakfast & brunch'),
        (1, 'lunch'),
        (2, 'dinner'),
        (3, 'appetizers & snacks'),
        (4, 'cocktails'),
    ]

    type_of_meal = models.IntegerField(choices=CHOICES)


class Ingredient(models.Model):
    name = models.CharField(max_length=128, unique=True)
    calories = models.PositiveSmallIntegerField()
    fat = models.PositiveSmallIntegerField()
    carbs = models.PositiveSmallIntegerField()
    protein = models.PositiveSmallIntegerField()


class IngredientMeasurement(models.Model):
    pass
