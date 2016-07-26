from django.test import TestCase
from .models import User
from .forms import UserRegistrationForm
from django import forms


# Create your tests here.


class CustomUserTest(TestCase):

    def test_manager_create(self):
        user = User.objects._create_user(None, 'test@test.com', 'password', False, False)
        self.assertIsNotNone(user)

        with self.assertRaises(ValueError):
            user = User.objects._create_user(None, None, 'password', False, False)

    def test_registration_form(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password1': 'let_me_in',
            'password2': 'let_me_in1',  # test for password matching
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError, "passwords do not match", form.full_clean())
