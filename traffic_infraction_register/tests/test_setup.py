from django.urls import reverse
from rest_framework.test import APITestCase
from django.test import TestCase
from django.contrib.auth.models import User


class APITestSetUp(APITestCase):

    def setUp(self):
        self.login_url = "/api/token/"


class TestSetUp(TestCase):

    def setUp(self):
        self.login_url = reverse("admin:login")
        user = dict(
            username="developer",
            first_name="developer",
            last_name="developer",
            password="developer",
            email="developer@mail.com",
        )
        self.superuser = User.objects.create_superuser(**user)

        self.client.login(username=self.superuser.username, password=user["password"])
