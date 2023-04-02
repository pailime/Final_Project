from urllib import request

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, FormView

from .forms import UserRegisterForm, AddIngredientMeasurementForm
from .models import Profile, Meal, TypeOfMeal, Ingredient, IngredientMeasurement


class MainPageView(View):
    def get(self, request):
        meals = Meal.objects.all()
        return render(
            request,
            'templates/Dish_Helper_app/base.html',
            context={'meals': meals}
        )


class ProfileLoginView(FormView):
    template_name = 'profile_form.html'
    success_url = 'base'

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        remember_me = form.cleaned_data.get('remember_me')
        if user is not None:
            login(self, request, user)
        if not remember_me:
            self.request.session.set_expiry(0)
        return super().form_valid(form)


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


class AddMealView(CreateView):
    model = Meal
    fields = ['name', 'description', 'recipe', 'total_time', 'servings']
    success_url = reverse_lazy('base')


class AddTypeOfMealView(CreateView):
    model = TypeOfMeal
    fields = ['type_of_meal']
    success_url = reverse_lazy('base')


class AddIngredientView(CreateView):
    model = Ingredient
    fields = ['name', 'calories', 'fat', 'carbs', 'protein']
    success_url = reverse_lazy('base')


# class AddIngredientMeasurementView(CreateView):
#     model = IngredientMeasurement
#     fields = ['weight']
#     success_url = reverse_lazy('base')


class AddIngredientMeasurementView(View):
    def get(self, request):
        measurement_form = AddIngredientMeasurementForm()
        context = {'measurement_form': measurement_form}
        return render(request, 'addingredientmeasurement_form.html', context)

    def post(self, request):
        measurement_form = AddIngredientMeasurementForm(request.POST)
        if measurement_form.is_valid():
            weight = measurement_form.cleaned_data['weight']
            ingredient_id = measurement_form.cleaned_data['ingredient_id']
            meal_id = measurement_form.cleaned_data['meal_id']
            measure = IngredientMeasurement.objects.create(weight=weight, ingredient_id=ingredient_id, meal_id=meal_id)
            context = {'measurement_form': measurement_form, 'measure': measure, 'weight': weight,
                       'ingredient_id': ingredient_id, 'meal_id': meal_id,}
            return render(request, 'base.html', context)
        else:
            context = {'measurement_form': measurement_form}
            return render(request, 'addingredientmeasurement_form.html', context)


# class MealSearchView(View):
#     def get(self, request):
#         search_form = MealSearchForm()
#         context = {'search_form': search_form, 'meals': 'empty'}
#         return render(request, 'navbar.html', context)
#
#     def post(self, request):
#         search_form = MealSearchForm(request.POST)
#         if search_form.is_valid():
#             name = search_form.cleaned_data['name']
#             meals = Meal.objects.filter(name__icontains=name)
#             return render(request, 'navbar.html',
#                           context={'meals': meals, 'search_form': search_form})
#         else:
#             context = {'search_form': search_form, 'meals': 'empty'}
#             return render(request, 'navbar.html', context)

