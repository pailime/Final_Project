import pytest
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client
from django.http import HttpResponse


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


def test_set_check_user(user):
    assert user.username == 'testuser'


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


def test_new_user(user_one):
    assert user_one.username == 'testuser'
    assert user_one.check_password('password')
    assert user_one.first_name == 'somename'
    assert user_one.last_name == 'somelast'
    assert user_one.email == 'whatever@test.com'
    assert user_one.is_superuser
    assert user_one.is_active


@pytest.mark.django_db
def test_add_meal(client, user_data):
    response = client.get('/add_meal/')
    assert response.status_code == 200
    response2 = client.get('')
    assert response2.status_code == 200

# @pytest.mark.django_db
# def test_add_meal_reverse(client):
#     response2 = client.get(reverse('base'))
#     assert response.status_code == 200


@pytest.mark.django_db
def test_add_type_url(client):
    response = client.get('/add_type/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_add_type_reverse(client):
    response = client.get(reverse('base'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_ingredient_url(client):
    response = client.get('/add_ingredient/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_add_ingredient_reverse(client):
    response = client.get(reverse('base'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_measurement_url(client):
    response = client.get('/add_measurement/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_add_measurement_reverse(client):
    response = client.get(reverse('base'))
    assert response.status_code == 200