from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile, Ingredient, Meal


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=128)
    last_name = forms.CharField(max_length=256)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class AddIngredientMeasurementForm(forms.Form):
    weight = forms.IntegerField(label='weight', min_value=0, max_value=10000)
    ingredient_id = forms.ModelChoiceField(
        label='ingredient id',
        queryset=Ingredient.objects.all(),
        widget=forms.Select
    )
    meal_id = forms.ModelChoiceField(
        label='meal id',
        queryset=Meal.objects.all(),
        widget=forms.Select
    )

