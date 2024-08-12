from tests.test_setup import TestSetUp
from django.urls import reverse
from faker import Faker

# Create your tests here.
from .models import Officer

faker = Faker()


class TestOfficerAdmin(TestSetUp):

    def test_officer_and_user_creation(self):
        new_officer = {
            "badge": f"{faker.city_prefix()}1234",
            "first_name": faker.first_name(),
            "last_name": faker.last_name(),
            "password": "1234",
        }
        self.client.post(reverse("admin:officers_officer_add"), data=new_officer)

        officer = Officer.objects.get(badge=new_officer["badge"])

        self.assertEqual(officer.user.username, new_officer["badge"])
