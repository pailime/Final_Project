import pytest
from django.contrib.auth import get_user_model
from django.test import Client
from Dish_Helper.Dish_Helper_app.views import ProfileLoginView


def client():
    client = Client
    return client


def test_exam_results(client):
    client.login(username='emilia', password='NoweHasło12!')
    response = client.get('base')
    assert response.status_code == 200

