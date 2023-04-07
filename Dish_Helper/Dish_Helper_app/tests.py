import pytest
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client


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
    # user.set_password("new-password")
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
    # assert user_one.password == 'password'
    assert user_one.first_name == 'somename'
    assert user_one.last_name == 'somelast'
    assert user_one.email == 'whatever@test.com'
    assert user_one.is_superuser
    assert user_one.is_active


class AddMealViewTest(TestCase):
    def test_view_url_at_desired_location(self):
        response = self.client.get('/add_meal/')
        self.assertEqual(response.status_code, 200)

