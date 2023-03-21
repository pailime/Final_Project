from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.views import View

from .models import User, Meal, TypeOfMeal, Ingredient, IngredientMeasurement


class MainPageView(View):
    def get(self, request):
        meals = Meal.objects.all()
        return render(
            request,
            'base.html',
            context={'meals': meals}
        )


class AddMealView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass
