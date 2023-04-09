import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client
from django.http import HttpResponse
from django.contrib.messages import get_messages
from Dish_Helper_app.models import Meal, TypeOfMeal, Ingredient, IngredientMeasurement


@pytest.mark.django_db
def test_login(client, user_data, user):
    url = reverse('login')
    response = client.post(url, data=user_data)
    assert response.status_code == 302
    assert response.url == reverse('base')
    assert client.login(**user_data) is True


@pytest.mark.django_db
def test_set_check_password(user):
    assert user.check_password('testpass') is True
    assert user.check_password('testpass1') is False


@pytest.mark.django_db
def test_set_check_user(user):
    assert user.username == 'testuser'


@pytest.mark.django_db
def test_new_user(user_one):
    assert user_one.username == 'testuser'
    assert user_one.check_password('password')
    assert user_one.first_name == 'somename'
    assert user_one.last_name == 'somelast'
    assert user_one.email == 'whatever@test.com'
    assert user_one.is_superuser
    assert user_one.is_active


@pytest.mark.django_db
def test_main_page(client, user):
    response = client.get('')
    assert response.status_code == 200


@pytest.mark.django_db
def test_meal_detail(client, user, meal):
    response = client.get(f'/mealdetail/{meal.id}/')
    assert response.status_code == 302
    assert response.url == (f'/accounts/login/?next=/mealdetail/{meal.id}/')
    client.force_login(user)
    response1 = client.get(f'/mealdetail/{meal.id}/')
    assert response1.status_code == 200


@pytest.mark.django_db
def test_add_meal(client, user, meal):
    response = client.get('/add_meal/')
    assert response.status_code == 302
    assert response.url == ('/login/?next=/add_meal/')
    client.force_login(user)
    response1 = client.get('/add_meal/')
    assert response1.status_code == 200
    response2 = client.post('/add_meal/', meal=meal)
    assert response2.status_code == 200
    assert Meal.objects.get(name=meal.name)
    print(meal.name)
    assert meal is not None


@pytest.mark.django_db
def test_add_type(client, user, type_of_meal):
    response = client.get('/add_type/')
    assert response.status_code == 302
    assert response.url == ('/login/?next=/add_type/')
    client.force_login(user)
    response1 = client.get('/add_type/')
    assert response1.status_code == 200
    response2 = client.post('/add_type/', type_of_meal=type_of_meal)
    assert response2.status_code == 200
    assert TypeOfMeal.objects.get(id=type_of_meal.id)
    assert type_of_meal is not None


@pytest.mark.django_db
def test_add_ingredient_url(client, user, ingredient):
    response = client.get('/add_ingredient/')
    assert response.status_code == 302
    assert response.url == ('/login/?next=/add_ingredient/')
    client.force_login(user)
    response1 = client.get('/add_ingredient/')
    assert response1.status_code == 200
    response2 = client.post('/add_ingredient/', ingredient=ingredient)
    assert response2.status_code == 200
    assert Ingredient.objects.get(name=ingredient.name)
    assert ingredient is not None


@pytest.mark.django_db
def test_add_measurement_url(client, user, ingredientmeasurement):
    response = client.get('/add_measurement/')
    assert response.status_code == 302
    assert response.url == ('/login/?next=/add_measurement/')
    client.force_login(user)
    response1 = client.get('/add_measurement/')
    assert response1.status_code == 200
    response2 = client.post('/add_measurement/', ingredientmeasurement=ingredientmeasurement)
    assert response2.status_code == 200
    assert IngredientMeasurement.objects.get(id=ingredientmeasurement.id)
    assert ingredientmeasurement is not None
