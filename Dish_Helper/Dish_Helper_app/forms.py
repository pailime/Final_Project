from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile, Ingredient


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=128)
    last_name = forms.CharField(max_length=256)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class MealForm(forms.Form):
    name = forms.CharField(label='Name', max_length=128)
    description = forms.CharField(label='Description:', widget=forms.Textarea)
    recipe = forms.CharField(label='Recipe:', widget=forms.Textarea)
    total_time = forms.IntegerField(label='Total preparation time in seconds', min_value=0, max_value=360)
    servings = forms.IntegerField(label='Number od servings')
    measurement = forms.ModelMultipleChoiceField(
        label='Ingedients:',
        queryset=Ingredient.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
