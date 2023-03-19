from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Meal(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()
    recipe = models.TextField()
    total_time = models.PositiveIntegerField()
    servings = models.PositiveSmallIntegerField()
    measurement = models.ManyToManyField('IngredientMeasurement')


class TypeOfMeal(models.Model):

    CHOICES = [
        (0, 'breakfast & brunch'),
        (1, 'lunch'),
        (2, 'dinner'),
        (3, 'appetizers & snacks'),
        (4, 'cocktails'),
    ]

    type_of_meal = models.IntegerField(choices=CHOICES)
    type = models.ForeignKey(Meal, on_delete=models.CASCADE)


class Ingredient(models.Model):
    name = models.CharField(max_length=128, unique=True)
    calories = models.PositiveSmallIntegerField()
    fat = models.PositiveSmallIntegerField()
    carbs = models.PositiveSmallIntegerField()
    protein = models.PositiveSmallIntegerField()


class IngredientMeasurement(models.Model):
    weight = models.PositiveSmallIntegerField()
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
