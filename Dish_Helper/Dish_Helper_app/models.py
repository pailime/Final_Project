from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user_name


class Meal(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True)
    recipe = models.TextField(null=True)
    total_time = models.PositiveIntegerField(null=True)
    servings = models.PositiveSmallIntegerField(null=True)
    measurement = models.ManyToManyField('Ingredient', through='IngredientMeasurement')

    def __str__(self):
        return self.name


class TypeOfMeal(models.Model):

    CHOICES = [
        (0, 'breakfast & brunch'),
        (1, 'lunch'),
        (2, 'dinner'),
        (3, 'appetizers & snacks'),
        (4, 'cocktails'),
    ]

    type_of_meal = models.IntegerField(choices=CHOICES)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.type_of_meal


class Ingredient(models.Model):
    name = models.CharField(max_length=128, unique=True)
    calories = models.PositiveSmallIntegerField(null=True)
    fat = models.PositiveSmallIntegerField(null=True)
    carbs = models.PositiveSmallIntegerField(null=True)
    protein = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return self.name


class IngredientMeasurement(models.Model):
    weight = models.PositiveSmallIntegerField(null=True)
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE, null=True)
    meal_id = models.ForeignKey(Meal, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.weight
