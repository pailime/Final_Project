import pytest
from django.contrib.auth import get_user_model
from django.test import RequestFactory
from .views import ProfileLoginView

User = get_user_model()

@pytest.mark.parametrize('username,password,authenticated', [
    ('emilia', 'NoweHasło23!', True),
    ('Małgorzata', 'Starehaslo123@', True),
    ('123jan', 'coNieco213!@', True)
])
def test_form_valid(username, password, authenticated):
    assert form_valid(username, password) == authenticated

