from django.test import TestCase
from django.contrib.auth.models import User
from places.models import Place


class PlaceModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser")
        self.place = Place.objects.create(
            name="Test Place",
            comments="This is a test place",
            latitude=11.0,
            longitude=12.0,
            author=self.user,
        )

    def test_create_place(self):
        place = Place.objects.create(
            name="Test Create Place",
            comments="This is a test create place",
            latitude=21.0,
            longitude=22.0,
            author=self.user,
        )

        fetched_place = Place.objects.get(id=place.id)

        # Test the attributes
        self.assertEqual(fetched_place.name, "Test Create Place")
        self.assertEqual(fetched_place.comments, "This is a test create place")
        self.assertEqual(fetched_place.latitude, 21.0)
        self.assertEqual(fetched_place.longitude, 22.0)
        self.assertEqual(fetched_place.author, self.user)
        self.assertIsNotNone(fetched_place.date)

    def test_name_label(self):
        place = Place.objects.get(id=1)
        field_label = place._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_comments_label(self):
        place = Place.objects.get(id=1)
        field_label = place._meta.get_field("comments").verbose_name
        self.assertEqual(field_label, "comments")

    def test_latitude_label(self):
        place = Place.objects.get(id=1)
        field_label = place._meta.get_field("latitude").verbose_name
        self.assertEqual(field_label, "latitude")

    def test_longitude_label(self):
        place = Place.objects.get(id=1)
        field_label = place._meta.get_field("longitude").verbose_name
        self.assertEqual(field_label, "longitude")

    def test_date_label(self):
        place = Place.objects.get(id=1)
        field_label = place._meta.get_field("date").verbose_name
        self.assertEqual(field_label, "date")

    def test_author_label(self):
        place = Place.objects.get(id=1)
        field_label = place._meta.get_field("author").verbose_name
        self.assertEqual(field_label, "author")

    def test_name_max_length(self):
        place = Place.objects.get(id=1)
        max_length = place._meta.get_field("name").max_length
        self.assertEqual(max_length, 75)

    def test_place_str_representation(self):
        self.assertEqual(str(self.place), "Test Place")

    def test_default_date_value(self):
        self.assertIsNotNone(self.place.date)

    def test_default_latitude_longitude(self):
        place = Place.objects.create(
            name="Test Place with Defaults",
            comments="This place uses default lat/lon",
            author=self.user,
        )
        self.assertEqual(place.latitude, 10.659190899078881)
        self.assertEqual(place.longitude, 106.72701745885105)
