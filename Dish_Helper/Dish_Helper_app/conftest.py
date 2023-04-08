import pytest
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client
from django.http import HttpResponse
from faker import Faker

fake = Faker()


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def user_data():
    return {
        'username': 'testuser',
        'password': 'testpass',
    }


@pytest.fixture
def user(db, user_data):
    return User.objects.create_user(**user_data)


@pytest.fixture
def new_user_one(db):
    def create_app_user(
            username: str,
            password: str = None,
            first_name: str = 'firstname',
            last_name: str = 'lastname',
            email: str = 'test@test.com',
            is_superuser: str = False,
            is_active: str = True,
    ):
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_superuser=is_superuser,
            is_active=is_active
        )
        return user
    return create_app_user


@pytest.fixture
def user_one(db, new_user_one):
    return new_user_one('testuser', 'password', 'somename', 'somelast', 'whatever@test.com', is_superuser='False', is_active='True')


@pytest.fixture
def meal():
    return Meal.objects.create(
        name=fake.words(nb=3),
        description=fake.sentence(),
        recipe=fake.sentence(nb=3),
        total_time=fake.random_int(min=10, max=50),
        servings=fake.random_int(min=1, max=10),
        measurement=Ingredient.objects.create(name=fake.word())
    )


@pytest.fixture
def type_of_meal():
    return TypeOfMeal.objects.create(
        type_of_meal=fake.random_int(min=0, max=5),
        meal=Meal.objects.create(name=fake.word())
    )


@pytest.fixture
def ingredient():
    return Ingredient.objects.create(
        name=fake.word(),
        calories=fake.random_int(min=1, max=1000),
        fat=fake.random_int(min=1, max=500),
        carbs=fake.random_int(min=1, max=500),
        protein=fake.random_int(min=1, max=500),
    )

@pytest.fixture
def ingredientmeasurement():
    return IngredientMeasurement.objects.create(
        weight=fake.random_int(min=1, max=500),
        meal_id=Meal.objects.create(name=fake.word()),
        ingredient_id=Ingredient.objects.create(name=fake.word())
    )

