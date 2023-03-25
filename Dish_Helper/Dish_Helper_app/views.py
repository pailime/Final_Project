from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.views import View
from django.views.generic import CreateView

from .models import User, Meal, TypeOfMeal, Ingredient, IngredientMeasurement


class MainPageView(View):
    def get(self, request):
        meals = Meal.objects.all()
        return render(
            request,
            'templates/Dish_Helper_app/base.html',
            context={'meals': meals}
        )


class AddMealView(CreateView):
    model = Meal
    fields = ['name', 'description', 'recipe', 'total_time', 'servings', 'measurement']


class AddTypeOfMealView(CreateView):
    model = TypeOfMeal
    fields = ['type_of_meal']


class AddIngredientView(CreateView):
    model = Ingredient
    fields = ['name', 'calories', 'fat', 'carbs', 'protein']


class AddIngredientMeasurementView(CreateView):
    model = IngredientMeasurement
    fields = ['weight']

