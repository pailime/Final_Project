import pytest
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client
from django.http import HttpResponse


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
def test_add_meal(client, user_data):
    response = client.get('/add_meal/')
    assert response.status_code == 302
    response2 = client.get('')
    assert response2.status_code == 200


@pytest.mark.django_db
def test_add_type_url(client):
    response = client.get('/add_type/')
    assert response.status_code == 302


@pytest.mark.django_db
def test_add_ingredient_url(client):
    response = client.get('/add_ingredient/')
    assert response.status_code == 302


@pytest.mark.django_db
def test_add_measurement_url(client):
    response = client.get('/add_measurement/')
    assert response.status_code == 302
