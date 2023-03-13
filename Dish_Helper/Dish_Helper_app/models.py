from django.db import models


class Meal(models.Model):

    CHOICES = [
        (0, 'breakfast & brunch'),
        (1, 'lunch'),
        (2, 'dinner'),
        (3, 'appetizers & snacks'),
        (4, 'cocktails'),
    ]

    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()
    recipe = models.TextField()
    total_time = models.PositiveIntegerField()
    # servings = models.PositiveSmallIntegerField()
    type_of_meal = models.IntegerField(choices=CHOICES)
    ingredients = models.ManyToManyField('Ingredient')


class Ingredient(models.Model):
    name = models.CharField(max_length=128, unique=True)
    calories = models.PositiveSmallIntegerField()
    fat = models.PositiveSmallIntegerField()
    carbs = models.PositiveSmallIntegerField()
    protein = models.PositiveSmallIntegerField()


