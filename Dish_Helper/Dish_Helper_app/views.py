import random
from urllib import request

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, FormView

from .forms import UserRegisterForm
from .models import Meal, TypeOfMeal, Ingredient, IngredientMeasurement


# View where authenticated User can find meal when choose ingredient
class MainPageView(View):
    def get_random_meal(self):
        return Meal.objects.order_by('?').first()

    def get(self, request):
        meals = list(Meal.objects.all())
        ingredients = Ingredient.objects.all()
        random_meal = self.get_random_meal()
        return render(
            request,
            'templates/Dish_Helper_app/home_page.html',
            context={'meals': meals, 'random_meal': random_meal, 'ingredients': ingredients}
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


# View with random meal details for authenticated user
class MealDetailView(LoginRequiredMixin, View):
    def get(self, request, id):
        meal_id = int(id)
        meal = get_object_or_404(Meal, id=meal_id)
        type = TypeOfMeal.objects.filter(meal=meal).first()
        ingredients = Ingredient.objects.filter(meal=meal)
        measure = IngredientMeasurement.objects.filter(meal_id=meal)
        context = {
            'meal': meal,
            'type': type,
            'ingredients': ingredients,
            'measure': measure
        }
        return render(request, 'templates/Dish_Helper_app/meal_detail.html', context)


# Profile user view
class ProfileLoginView(FormView):
    template_name = 'templates/Dish_Helper_app/profile_form.html'
    success_url = 'base'

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user is not None:
            login(self, request, user)
            messages.success(self.request, "You've been logged in")
        return super().form_valid(form)


# Registration view
class ProfileRegisterView(View):
    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You are now able to log in.')
            return redirect('base')
        else:
            error_messages = list(form.errors.values())
            for message in error_messages:
                messages.error(request, message)
            return redirect('register')

    def get(self, request):
        form = UserRegisterForm()
        context = {'form': form}
        return render(request, 'templates/Dish_Helper_app/register.html', context)


# View where authenticated user can add meal
class AddMealView(LoginRequiredMixin, CreateView):
    model = Meal
    fields = ['name', 'description', 'recipe', 'total_time', 'servings', 'measurement']
    success_url = reverse_lazy('base')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Meal was added successfully.')
        return response


# View where authenticated user can add type of meal
class AddTypeOfMealView(LoginRequiredMixin, CreateView):
    model = TypeOfMeal
    fields = ['type_of_meal', 'meal']
    success_url = reverse_lazy('base')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Type of meal was added successfully.')
        return response


# View where authenticated user can add ingredient
class AddIngredientView(LoginRequiredMixin, CreateView):
    model = Ingredient
    fields = ['name', 'calories', 'fat', 'carbs', 'protein']
    success_url = reverse_lazy('base')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Ingredient was added successfully.')
        return response


# View where authenticated user can add ingredient measurement
class AddIngredientMeasurementView(LoginRequiredMixin, CreateView):
    model = IngredientMeasurement
    fields = ['weight', 'ingredient_id', 'meal_id']
    success_url = reverse_lazy('base')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Ingredient Measurement was added successfully.')
        return response
