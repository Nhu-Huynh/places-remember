from django import forms
from django.test import TestCase
from places.forms import PlaceForm
from django.contrib.auth.models import User


class PlaceFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser")

    def test_form_fields(self):
        form = PlaceForm()
        expected_fields = ["name", "latitude", "longitude", "comments"]
        self.assertEqual(list(form.fields), expected_fields)

    def test_form_field_widgets(self):
        form = PlaceForm()
        self.assertIsInstance(form.fields["latitude"].widget, forms.HiddenInput)
        self.assertIsInstance(form.fields["longitude"].widget, forms.HiddenInput)

    def test_form_validation_with_valid_data(self):
        form_data = {
            "name": "Test Place",
            "latitude": 10.0,
            "longitude": 20.0,
            "comments": "This is a test place",
        }
        form = PlaceForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_validation_with_missing_name(self):
        form_data = {
            "name": "",
            "latitude": 10.0,
            "longitude": 20.0,
            "comments": "This is a test place",
        }
        form = PlaceForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)

    def test_form_validation_with_invalid_latitude_longitude(self):
        form_data = {
            "name": "Test Place",
            "latitude": "invalid",
            "longitude": "invalid",
            "comments": "This is a test place",
        }
        form = PlaceForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("latitude", form.errors)
        self.assertIn("longitude", form.errors)

    def test_form_save(self):
        form_data = {
            "name": "Test Place",
            "latitude": 10.0,
            "longitude": 20.0,
            "comments": "This is a test place",
            "author_id": self.user.id,
        }
        form = PlaceForm(data=form_data)
        self.assertTrue(form.is_valid())
        place = form.save(commit=False)
        place.author = self.user
        place.save()
        self.assertEqual(place.name, "Test Place")
        self.assertEqual(place.latitude, 10.0)
        self.assertEqual(place.longitude, 20.0)
        self.assertEqual(place.comments, "This is a test place")
        self.assertEqual(place.author, self.user)
