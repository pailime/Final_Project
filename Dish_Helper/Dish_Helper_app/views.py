from urllib import request

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, FormView

from .forms import UserRegisterForm
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

