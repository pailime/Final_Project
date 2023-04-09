import pytest
from django.urls import reverse
from Dish_Helper_app.models import Meal, TypeOfMeal, Ingredient, IngredientMeasurement
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_login(client, user_data, user):
    """
    This test checks the login functionality of the Django application.
    :param client:
    :param user_data:
    :param user:
    :return:
    """
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
def test_meal_detail(client, user, meal, user_data):
    response = client.get(f'/mealdetail/{meal.id}/')
    assert response.status_code == 302
    assert response.url == f'/accounts/login/?next=/mealdetail/{meal.id}/'
    response3 = client.get(f'/mealdetail/{not meal.id}/')
    assert response3.status_code == 404
    client.force_login(user)
    response1 = client.get(f'/mealdetail/{meal.id}/')
    assert response1.status_code == 200
    assert client.login(**user_data) is True
    response2 = client.get(f'/mealdetail/{not meal.id}/')
    assert response2.status_code == 404



@pytest.mark.django_db
def test_add_meal(client, user, meal, user_data):
    response = client.get('/add_meal/')
    assert response.status_code == 302
    assert response.url == '/login/?next=/add_meal/'
    client.force_login(user)
    response1 = client.get('/add_meal/')
    assert response1.status_code == 200
    assert client.login(**user_data) is True
    response2 = client.post('/add_meal/', meal=meal)
    assert response2.status_code == 200
    assert Meal.objects.get(name=meal.name)
    print(meal.name)
    assert meal is not None
    assertTemplateUsed(response2, 'templates/Dish_Helper_app/meal_form.html')


@pytest.mark.django_db
def test_add_type(client, user, type_of_meal, user_data):
    response = client.get('/add_type/')
    assert response.status_code == 302
    assert response.url == '/login/?next=/add_type/'
    client.force_login(user)
    response1 = client.get('/add_type/')
    assert response1.status_code == 200
    assert client.login(**user_data) is True
    response2 = client.post('/add_type/', type_of_meal=type_of_meal)
    assert response2.status_code == 200
    assert TypeOfMeal.objects.get(id=type_of_meal.id)
    print(type_of_meal.type_of_meal)
    assert type_of_meal is not None
    assertTemplateUsed(response2, 'templates/Dish_Helper_app/typeofmeal_form.html')


@pytest.mark.django_db
def test_add_ingredient(client, user, ingredient, user_data):
    response = client.get('/add_ingredient/')
    assert response.status_code == 302
    assert response.url == '/login/?next=/add_ingredient/'
    client.force_login(user)
    response1 = client.get('/add_ingredient/')
    assert response1.status_code == 200
    assert client.login(**user_data) is True
    response2 = client.post('/add_ingredient/', ingredient=ingredient)
    assert response2.status_code == 200
    assert Ingredient.objects.get(name=ingredient.name)
    print(ingredient.name)
    assert ingredient is not None
    assertTemplateUsed(response2, 'templates/Dish_Helper_app/ingredient_form.html')


@pytest.mark.django_db
def test_add_measurement(client, user, ingredientmeasurement):
    response = client.get('/add_measurement/')
    assert response.status_code == 302
    assert response.url == '/login/?next=/add_measurement/'
    client.force_login(user)
    response1 = client.get('/add_measurement/')
    assert response1.status_code == 200
    response2 = client.post('/add_measurement/', ingredientmeasurement=ingredientmeasurement)
    assert response2.status_code == 200
    assert IngredientMeasurement.objects.get(id=ingredientmeasurement.id)
    print(ingredientmeasurement.id)
    assert ingredientmeasurement is not None
    assertTemplateUsed(response2, 'templates/Dish_Helper_app/ingredientmeasurement_form.html')
