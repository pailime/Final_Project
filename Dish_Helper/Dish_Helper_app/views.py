from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .models import User, Meal, TypeOfMeal, Ingredient, IngredientMeasurement


class MainPageView(View):
    pass