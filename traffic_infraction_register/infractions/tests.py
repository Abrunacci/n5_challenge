import json
import random
from tests.test_setup import TestSetUp
from rest_framework import status
from django.urls import reverse
from faker import Faker

from officers.models import Officer
from persons.models import Person
from vehicles.models import Vehicle

# Create your tests here.
from .models import Infraction


faker = Faker()


class TestInfractions(TestSetUp):

    def setUp(self):
        super(TestInfractions, self).setUp()

        new_officer = {
            "badge": f"{faker.city_prefix()}1234",
            "first_name": faker.first_name(),
            "last_name": faker.last_name(),
            "password": "1234",
        }
        self.client.post(reverse("admin:officers_officer_add"), data=new_officer)

        self.officer = Officer.objects.get(badge=new_officer["badge"])

        self.persons = [
            Person.objects.create(**data)
            for data in [
                {"full_name": faker.name(), "email": faker.email()},
                {"full_name": faker.name(), "email": faker.email()},
                {"full_name": faker.name(), "email": faker.email()},
                {"full_name": faker.name(), "email": faker.email()},
                {"full_name": faker.name(), "email": faker.email()},
            ]
        ]

        self.vehicles = list()

        for person in self.persons:
            vehicle = Vehicle.objects.create(
                brand="Ford",
                color=faker.color(),
                license_plate=faker.license_plate(),
                owner=person,
            )
            self.vehicles.append(vehicle)

    def test_save_infraction(self):
        random_vehicle_pick = random.choice(self.vehicles)
        infraction_data = {
            "date": faker.date("%Y-%m-%d"),
            "license_plate": random_vehicle_pick.license_plate,
            "type": random.choice(["parking", "speeding", "red light"]),
            "description": "A new ticket for you",
            "amount": 2554.25,
        }
        login_response = self.client.post(
            reverse("token_obtain_pair"),
            data={"username": self.officer.badge, "password": "1234"},
            format="json",
        )
        token = f"Bearer {login_response.data['access']}"
        response = self.client.post(
            reverse("infractions_api"),
            json.dumps(infraction_data),
            headers={"Authorization": token},
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        infractions = Infraction.objects.all()
        self.assertEqual(infractions.count(), 1)
        self.assertEqual(infractions[0].person, random_vehicle_pick.owner)
        self.assertEqual(infractions[0].vehicle, random_vehicle_pick)
        self.assertEqual(infractions[0].officer, self.officer)

    def test_save_infraction_404(self):
        infraction_data = {
            "date": faker.date("%Y-%m-%d"),
            "license_plate": "a",
            "type": random.choice(["parking", "speeding", "red light"]),
            "description": "A new ticket for you",
            "amount": 2554.25,
        }
        login_response = self.client.post(
            reverse("token_obtain_pair"),
            data={"username": self.officer.badge, "password": "1234"},
            format="json",
        )
        token = f"Bearer {login_response.data['access']}"
        response = self.client.post(
            reverse("infractions_api"),
            json.dumps(infraction_data),
            headers={"Authorization": token},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_save_infraction_400(self):
        random_vehicle_pick = random.choice(self.vehicles)
        infraction_data = {
            "date": faker.date("%Y-%m-%d"),
            "license_plate": random_vehicle_pick.license_plate,
            "type": random.choice(["parking", "speeding", "red light"]),
            "description": "A new ticket for you",
            "amount": -2554.25,
        }
        login_response = self.client.post(
            reverse("token_obtain_pair"),
            data={"username": self.officer.badge, "password": "1234"},
            format="json",
        )
        token = f"Bearer {login_response.data['access']}"
        response = self.client.post(
            reverse("infractions_api"),
            json.dumps(infraction_data),
            headers={"Authorization": token},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
