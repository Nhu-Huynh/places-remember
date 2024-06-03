from django.test import TestCase, Client
from django.contrib.auth.models import User
from places.models import Place
from django.urls import reverse


class PlaceViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.client.login(username="testuser", password="12345")

        self.place = Place.objects.create(
            name="Test Place", comments="Test Comment", author=self.user
        )

    def test_place_new_view_get(self):
        response = self.client.get(reverse("places:place_new"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "place_new.html")

    def test_place_new_view_post(self):
        response = self.client.post(
            reverse("places:place_new"),
            {
                "name": "New Place",
                "comments": "New Comment",
                "latitude": 10.659190899078881,
                "longitude": 106.72701745885105,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Place.objects.filter(name="New Place").exists())

    def test_place_update_view_get(self):
        response = self.client.get(reverse("places:place_update", args=[self.place.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "place_new.html")
        self.assertContains(response, self.place.name)

    def test_place_update_view_post(self):
        response = self.client.post(
            reverse("places:place_update", args=[self.place.id]),
            {
                "name": "Updated Place",
                "comments": "Updated Comment",
                "latitude": 10.659190899078881,
                "longitude": 106.72701745885105,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.place.refresh_from_db()
        self.assertEqual(self.place.name, "Updated Place")
        self.assertEqual(self.place.comments, "Updated Comment")

    def test_place_delete_view_get(self):
        response = self.client.get(reverse("places:place_delete", args=[self.place.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "place_confirm_delete.html")

    def test_place_delete_view_post(self):
        response = self.client.post(
            reverse("places:place_delete", args=[self.place.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Place.objects.filter(id=self.place.id).exists())

    def test_place_new_view_unauthenticated(self):
        self.client.logout()
        response = self.client.get(reverse("places:place_new"))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/?next=/places/new/")

    def test_place_update_view_unauthenticated(self):
        self.client.logout()
        response = self.client.get(reverse("places:place_update", args=[self.place.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, f"/?next=/places/edit/{self.place.id}/")

    def test_place_delete_view_unauthenticated(self):
        self.client.logout()
        response = self.client.get(reverse("places:place_delete", args=[self.place.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, f"/?next=/places/delete/{self.place.id}/")
