import random
from urllib import request

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, FormView

from .forms import UserRegisterForm
from .models import Meal, TypeOfMeal, Ingredient, IngredientMeasurement


# View where authenticated User can find meal when choose ingredient
class MainPageView(View):
    def get(self, request):
        meals = list(Meal.objects.all())
        ingredients = Ingredient.objects.all()
        for m in meals:
            random.shuffle(meals)
        meal1 = meals[0]
        return render(
            request,
            'templates/Dish_Helper_app/home_page.html',
            context={'meals': meals, 'meal1': meal1, 'ingredients': ingredients}
        )

    def post(self, request):
        ingredient_id = request.POST.get('ingredient')
        ingredient = Ingredient.objects.get(pk=ingredient_id)
        meals = Meal.objects.filter(ingredientmeasurement__ingredient_id=ingredient)
        return render(
            request,
            'templates/Dish_Helper_app/home_page.html',
            context={'meals': meals, 'ingredient': ingredient}
        )


# View with random meal details
class MealDetailView(View):
    def get(self, request, id):
        meal_id = int(id)
        meal = Meal.objects.get(id=meal_id)
        context = {'meal': meal}
        return render(request, 'mealdetail.html', context)


# Profile user view
class ProfileLoginView(FormView):
    template_name = 'profile_form.html'
    success_url = 'base'

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user is not None:
            login(self, request, user)
        return super().form_valid(form)


# Registration view
class ProfileRegisterView(View):
    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
        else:
            return redirect('register')

    def get(self, request):
        form = UserRegisterForm()
        context = {'form': form}
        return render(request, 'register.html', context)


# View where authenticated user can add meal
class AddMealView(CreateView):
    model = Meal
    fields = ['name', 'description', 'recipe', 'total_time', 'servings', 'measurement']
    success_url = reverse_lazy('base')


# View where authenticated user can add type of meal
class AddTypeOfMealView(CreateView):
    model = TypeOfMeal
    fields = ['type_of_meal', 'meal']
    success_url = reverse_lazy('base')


# View where authenticated user can add ingredient
class AddIngredientView(CreateView):
    model = Ingredient
    fields = ['name', 'calories', 'fat', 'carbs', 'protein']
    success_url = reverse_lazy('base')


# View where authenticated user can add ingredient measurement
class AddIngredientMeasurementView(CreateView):
    model = IngredientMeasurement
    fields = ['weight', 'ingredient_id', 'meal_id']
    success_url = reverse_lazy('base')
