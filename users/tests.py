from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from places.models import Place
from django.urls import reverse

from allauth.socialaccount.models import SocialApp
from django.contrib.sites.shortcuts import get_current_site
import os
from dotenv import load_dotenv

load_dotenv()


class HomeViewTest(TestCase):
    def setUp(self):
        # Create a request factory instance
        self.factory = RequestFactory()
        request = self.factory.get("/")

        # Create SocialApp for Google login
        sa = SocialApp.objects.create(
            provider="google",
            name="Google",
            client_id=os.getenv("GOOGLE_CLIENT_ID"),
            secret=os.getenv("GOOGLE_CLIENT_SECRET"),
        )
        sa.sites.add(get_current_site(request))

        # Create a user
        self.user = User.objects.create_user(username="testuser", password="12345")

        # Log in the user
        self.client = Client()
        self.client.login(username="testuser", password="12345")

        # Create multiple Place instances
        number_of_places = 7
        for i in range(number_of_places):
            Place.objects.create(
                name=f"Place {i}",
                comments=f"Comment {i}",
                author=self.user,
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_view_uses_correct_template(self):
        response = self.client.get(reverse("users:home"))
        self.assertTemplateUsed(response, "home.html")

    def test_home_view_pagination(self):
        response = self.client.get(reverse("users:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTrue("page_obj" in response.context)
        page_obj = response.context["page_obj"]

        self.assertEqual(page_obj.paginator.num_pages, 2)
        self.assertEqual(len(page_obj), 5)  # 5 items per page

    def test_home_view_lists_all_places(self):
        response = self.client.get(reverse("users:home") + "?page=2")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("page_obj" in response.context)
        self.assertEqual(len(response.context["page_obj"]), 2)  # Remaining 2 items

    def test_home_view_content(self):
        response = self.client.get(reverse("users:home"))
        self.assertEqual(response.status_code, 200)

        place_list = response.context["page_obj"].object_list
        place_name_list = []
        for place in place_list:
            place_name_list.append(place.name)

        for i in range(6, 1, -1):
            self.assertIn(f"Place {i}", place_name_list)

        # Test the second page
        response = self.client.get(reverse("users:home"), {"page": 2})
        self.assertEqual(response.status_code, 200)

        place_list = response.context["page_obj"].object_list
        place_name_list = []
        for place in place_list:
            place_name_list.append(place.name)

        # Check 'Place 0' and 'Place 1' are in the second page
        self.assertIn("Place 0", place_name_list)
        self.assertIn("Place 1", place_name_list)

        # Check 'Place 6' and 'Place 5' are not in the second page
        self.assertNotIn("Place 6", place_name_list)
        self.assertNotIn("Place 5", place_name_list)
