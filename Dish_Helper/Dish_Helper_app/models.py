from django.db import models


class Meal(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()
    preparation = models.TextField()
    preparation_time = models.PositiveIntegerField()
    portions = models.PositiveSmallIntegerField()


class Ingredients(models.Model):
    name = models.CharField(max_length=128, unique=True)
