from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from .models import Profile, Meal, TypeOfMeal, Ingredient, IngredientMeasurement


class MainPageView(View):
    def get(self, request):
        meals = Meal.objects.all()
        return render(
            request,
            'templates/Dish_Helper_app/base.html',
            context={'meals': meals}
        )


class ProfileLoginView(LoginView):
    template_name = 'profile_form.html'
    success_url = reverse_lazy('base')

    def form_valid(self, form):
        response = super().form_valid(form)
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)
        return response


class AddMealView(View):
    meal = Meal.objects.all()
    type = TypeOfMeal.objects.all()
    ingredient = Ingredient.objects.all()
    measurement = IngredientMeasurement.objects.all()
    pass

    # model = Meal
    # fields = ['name', 'description', 'recipe', 'total_time', 'servings', 'measurement']


class AddTypeOfMealView(CreateView):
    model = TypeOfMeal
    fields = ['type_of_meal']


class AddIngredientView(CreateView):
    model = Ingredient
    fields = ['name', 'calories', 'fat', 'carbs', 'protein']


class AddIngredientMeasurementView(CreateView):
    model = IngredientMeasurement
    fields = ['weight']

