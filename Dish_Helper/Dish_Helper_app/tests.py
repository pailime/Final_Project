import pytest
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


