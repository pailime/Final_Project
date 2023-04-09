import pytest
from django.urls import reverse
from Dish_Helper_app.models import Meal, TypeOfMeal, Ingredient, IngredientMeasurement
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_login(client, user_data, user):
    """
    Test that a user can log in successfully.

    :param client: Django test client object.
    :param user_data: A fixture with user credentials (default {'username': 'testuser', 'password': 'testpass'}).
    :param user: A user object to use for authentication.
    :type user: django.contrib.auth.models.User
    """
    url = reverse('login')
    response = client.post(url, data=user_data)
    assert response.status_code == 302
    assert response.url == reverse('base')
    assert client.login(**user_data) is True


@pytest.mark.django_db
def test_set_check_password(user):
    """
    Test that a user's password can be set and checked correctly.
    """
    assert user.check_password('testpass') is True
    user.set_password('newpass')
    user.save()
    assert user.check_password('newpass') is True
    assert user.check_password('testpass') is False


@pytest.mark.django_db
def test_set_check_user(user):
    """
    Test that a user's username is set correctly.
    """
    assert user.username == 'testuser'


@pytest.mark.django_db
def test_new_user(user_one):
    """
    Test that a new user is created with the expected attributes.

    :param user_one: A fixture that creates a user with the given credentials.
    :type user_one: django.contrib.auth.models.User
    """
    assert user_one.username == 'testuser'
    assert user_one.check_password('password')
    assert user_one.first_name == 'somename'
    assert user_one.last_name == 'somelast'
    assert user_one.email == 'whatever@test.com'
    assert user_one.is_superuser
    assert user_one.is_active


@pytest.mark.django_db
def test_main_page(client, user, meal):
    """
    Test that the main page view returns a 200 status code and renders the correct template.
    Also tests that the response contains the correct context data.

    :param meal: A meal object to test with.
    """
    response = client.get('')
    assert response.status_code == 200
    assert 'meals' in response.context
    assert 'random_meal' in response.context
    assert 'ingredients' in response.context
    assertTemplateUsed(response, 'templates/Dish_Helper_app/home_page.html')


@pytest.mark.django_db
def test_meal_detail(client, user, meal, user_data):
    """
    Test that the meal detail view returns the correct HTTP status codes and templates,
    and that unauthorized users are redirected to the login page.
    """
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
    """
    This test case checks the add meal functionality by testing the status code of the responses when trying to access
    the add meal page both authenticated and unauthenticated, making a post request with a meal object to create a new
    meal, and checking that the meal was created successfully.
    """
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
    """
    This test case checks the add type functionality by testing the status code of the responses when trying to access
    the add type page both authenticated and unauthenticated, making a post request with a type_of_meal object to create
     a new type_of_meal, and checking that the type_of_meal was created successfully.

    :param type_of_meal: A type_of_meal object to use for testing.
    """
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
    """
    This test case checks the add ingredient functionality by testing the status code of the responses when trying to
    access the add ingredient page both authenticated and unauthenticated, making a post request with an ingredient
    object to create a new ingredient, and checking that the ingredient was created successfully.

    :param ingredient: An ingredient object to use for testing.
    """
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
    """
    This test case checks the add measurement functionality by testing the status code of the responses when trying to
    access the add measurement page both authenticated and unauthenticated, making a post request with an
    ingredientmeasurement object to create a new measurement, and checking that the measurement was created successfully

    :param ingredientmeasurement: An ingredientmeasurement object to use for testing.
    """
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
