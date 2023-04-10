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


class ProfileLoginView(FormView):
    """
    View for handling user login via a form submission.
    This view displays a form where users can enter their username and password.
    Upon form submission, the view attempts to authenticate the user with Django's authentication system.
    If authentication is successful, the user is logged in and redirected to the 'base' URL.
    If authentication fails, an error message is displayed and the user is prompted to try again.

    Attributes:
        template_name (str): The path to the template for this view.
        success_url (str): The URL to redirect to upon successful form submission.

    Methods:
        form_valid: Handle a valid form submission.
    """
    template_name = 'templates/Dish_Helper_app/profile_form.html'
    success_url = 'base'

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user is not None:
            login(self, request, user)
            messages.success(self.request, "You've been logged in")
        return super().form_valid(form)


class ProfileRegisterView(View):
    """
    View for handling user registration via a form submission.
    This view displays a form where users can enter their desired username, email address, and password.
    Upon form submission, the view attempts to validate the form data.
    If validation is successful, the view creates a new user account and redirects the user to the 'base' URL.
    If validation fails, error messages are displayed and the user is prompted to try again.
    """
    def post(self, request):
        """
        Handle a POST request to register a new user account.

        :param request: The HTTP request object.
        :return: A redirect response to the home page if registration is successful,
                 or a redirect response to the registration page if registration fails.
        """
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
        """
        Display the user registration form.
        :param request: the HTTP request object.
        :return: the HTTP response object with the rendered register.html template.
        """
        form = UserRegisterForm()
        context = {'form': form}
        return render(request, 'templates/Dish_Helper_app/register.html', context)


class MainPageView(View):
    """
    View for the home page of the Dish Helper app.
    This view has two main functionalities: displaying a random meal and allowing users to filter meals by ingredient.
    """

    def get_random_meal(self):
        """
        Get a random meal from the database.

        :return: A randomly selected meal.
        """
        return Meal.objects.order_by('?').first()

    def get(self, request):
        """
        Handle GET requests to the home page.

        :param request: The HTTP request object.
        :return: The rendered HTML page containing the home page.
        """
        meals = list(Meal.objects.all())
        ingredients = Ingredient.objects.all()
        random_meal = self.get_random_meal()
        return render(
            request,
            'templates/Dish_Helper_app/home_page.html',
            context={'meals': meals, 'random_meal': random_meal, 'ingredients': ingredients}
        )

    def post(self, request):
        """
        Handle POST requests to filter meals by ingredient.

        :param request: The HTTP request object.
        :return: The rendered HTML page containing the filtered meals.
        """
        ingredient_id = request.POST.get('ingredient')
        ingredient = Ingredient.objects.get(pk=ingredient_id)
        meals = Meal.objects.filter(ingredientmeasurement__ingredient_id=ingredient)
        return render(
            request,
            'templates/Dish_Helper_app/home_page.html',
            context={'meals': meals, 'ingredient': ingredient}
        )


class MealDetailView(LoginRequiredMixin, View):
    """
    View for displaying details of a Meal object.
    This view displays the name, type, ingredients, and measurements for a single Meal object.
    Only logged-in users can access this page.
    """
    def get(self, request, id):
        """
        Handle GET requests to the Meal Detail page.

        :param request: The HTTP request object.
        :param id: The ID of the meal to view.
        :return: The rendered HTML page containing the details of the meal.
        """
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


class AddMealView(LoginRequiredMixin, CreateView):
    """
    View for adding a new Meal object via a form submission.
    This view allows authenticated users to create new Meal objects by submitting a form with the required data.
    The form includes fields for the meal's name, description, recipe, total time, number of servings, and measurement.

    Attributes:
        model (Meal): The model class for creating new Meal objects.
        fields (list of str): The list of fields from the Meal model that should be included in the form.
        success_url (str): The URL to redirect to after a successful form submission.
        login_url (str): The URL to redirect to if a user attempts to access this view while not authenticated.

    Methods:
        form_valid(form): Handle a valid form submission.
    """
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
    """
    View for adding a new TypeOfMeal object via a form submission.
    This view allows authenticated users to create new TypeOfMeal objects by submitting a form with the required data.
    The form includes fields for the TypeOfMeal type_of_meal and meal.

    Attributes:
        model (TypeOfMeal): The model class for creating new TypeOfMeal objects.
        fields (list of str): The list of fields from the TypeOfMeal model that should be included in the form.
        success_url (str): The URL to redirect to after a successful form submission.
        login_url (str): The URL to redirect to if a user attempts to access this view while not authenticated.

    Methods:
        form_valid(form): Handle a valid form submission.
    """
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
    """
    View for adding a new Ingredient object via a form submission.
    This view allows authenticated users to create new Ingredient objects by submitting a form with the required data.
    The form includes fields for the Ingredient name, calories, fat, carbs and protein.

    Attributes:
        model (Ingredient): The model class for creating new Ingredient objects.
        fields (list of str): The list of fields from the Ingredient model that should be included in the form.
        success_url (str): The URL to redirect to after a successful form submission.
        login_url (str): The URL to redirect to if a user attempts to access this view while not authenticated.

    Methods:
        form_valid(form): Handle a valid form submission.
    """
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
    """
    View for adding a new IngredientMeasurement object via a form submission.
    This view allows authenticated users to create new IngredientMeasurement objects by submitting a form with the
    required data.
    The form includes fields for the IngredientMeasurement weight, ingredient_id and meal_id.

    Attributes:
        model (IngredientMeasurement): The model class for creating new Ingredient objects.
        fields (list of str): The list of fields from the IngredientMeasurement model that should be included in
                              the form.
        success_url (str): The URL to redirect to after a successful form submission.
        login_url (str): The URL to redirect to if a user attempts to access this view while not authenticated.

    Methods:
        form_valid(form): Handle a valid form submission.
    """
    model = IngredientMeasurement
    fields = ['weight', 'ingredient_id', 'meal_id']
    success_url = reverse_lazy('base')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Ingredient Measurement was added successfully.')
        return response
