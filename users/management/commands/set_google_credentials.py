# your_app/management/commands/set_google_credentials.py
from django.core.management.base import BaseCommand
from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site
import os
from dotenv import load_dotenv

load_dotenv()


class Command(BaseCommand):
    help = "Set Google social account credentials from environment variables"

    def handle(self, *args, **kwargs):
        site = Site.objects.get(pk=3)
        app, created = SocialApp.objects.get_or_create(
            provider="google", defaults={"name": "Google"}
        )
        client_id = os.getenv("GOOGLE_CLIENT_ID")
        client_secret = os.getenv("GOOGLE_CLIENT_SECRET")

        print("client_id:", client_id)
        print("client_secret:", client_secret)

        app.client_id = client_id
        app.secret = client_secret
        app.sites.add(site)
        app.save()
        self.stdout.write(
            self.style.SUCCESS("Successfully set Google social account credentials")
        )
