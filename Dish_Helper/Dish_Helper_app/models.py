from django.db import models


class Meal(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()
    recipe = models.TextField()
    total_time = models.PositiveIntegerField()
    servings = models.PositiveSmallIntegerField()
    ingredients = models.ManyToManyField('Ingredient')


class Ingredient(models.Model):
    name = models.CharField(max_length=128, unique=True)
    calories = models.PositiveSmallIntegerField()
    fat = models.PositiveSmallIntegerField()
    carbs = models.PositiveSmallIntegerField()
    protein = models.PositiveSmallIntegerField()

