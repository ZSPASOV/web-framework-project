from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import SignUpForm, ProfileForm
from .models import Profile
import datetime
from django.contrib.auth import get_user_model

# Create your tests here.

class ProfileTest(TestCase):

    @classmethod
    def setUp(cls):
        cls.testuser = get_user_model().objects.create_user(
                username='testuser', email='testing@gmail.com',
                password='test@1234')

    def test_valid_data_signup_form(self):
        form = SignUpForm({
            'first_name': "test",
            'last_name': "user",
            'email': "test@gmail.com",
            'username': "tuser",
            'password1': "test@123",
            'password2': "test@123",
        })
        self.assertTrue(form.is_valid())
        signup = form.save()
        self.assertEqual(signup.first_name, "test")
        self.assertEqual(signup.email, "test@gmail.com")
        self.assertEqual(signup.last_name, "user")
        self.assertEqual(signup.username, "tuser")

    def test_blank_data_signup_form(self):
        form = SignUpForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(dict(form.errors.items()), 
        {
            "username": ["This field is required."],
            "password1": ["This field is required."],
            "password2": ["This field is required."],
            "email": ["This field is required."],
            "first_name": ["This field is required."],
            "last_name": ["This field is required."]
            })


    def test_valid_data_profile_form(self):
        form = ProfileForm({
            'user': self.testuser,
            'bio': "This is test introduction",
            'phone': "+12125552378",
            'location': "Paris",
            'birth_date': datetime.datetime.now().date(),
            'image': 'None'
        })
        self.assertFalse(form.is_valid())


    def test_blank_data_profile_form(self):
        form = ProfileForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(dict(form.errors.items()), 
        {
            "user": ["This field is required."],
            "phone": ["This field is required."],
            "image": ["This field is required."],
            })


    def test_with_authenticate_user_profile_update(self):
        self.client.force_login(user=self.testuser)
        form_data= {
            'user': self.testuser,
            'bio': "This is test introduction",
            'phone': "+12125552378",
            'location': "Paris",
            'birth_date': datetime.datetime.now().date(),
            'image': 'None'
        }
        response = self.client.get(reverse('edit-profile',kwargs={'pk':self.testuser.id}),data=form_data)
        self.assertTrue(response.status_code == 200)

    def test_with_unauthenticate_user_profile_update(self):
        form_data= {
            'user': self.testuser,
            'bio': "This is test introduction",
            'phone': "+12125552378",
            'location': "Paris",
            'birth_date': datetime.datetime.now().date(),
            'image': 'None'
        }
        # with self.assertRaises(TypeError):
        response = self.client.get(reverse('edit-profile',kwargs={'pk':self.testuser.id}),data=form_data)
        self.assertTrue(response.status_code == 302)
