from django.db.utils import IntegrityError
from django.test import TestCase
from faker import Faker

from persons.models import Person
from .models import Vehicle


faker = Faker()


class TestVehicle(TestCase):
    def setUp(self):
        self.owner_one = Person.objects.create(
            full_name="Person One", email="person@one.com"
        )
        self.owner_two = Person.objects.create(
            full_name="Person Two", email="person@two.com"
        )

    def test_vehicle_creation(self):
        Vehicle.objects.create(
            license_plate="AB123CD", color="Red", brand="GM", owner=self.owner_one
        )
        created_vehicle = Vehicle.objects.get(pk="AB123CD")
        self.assertEqual(created_vehicle.color, "Red")
        self.assertEqual(created_vehicle.brand, "GM")
        self.assertEqual(created_vehicle.owner, self.owner_one)

    def test_vehicle_change_owner(self):
        Vehicle.objects.create(
            license_plate="AB123CD", color="Red", brand="GM", owner=self.owner_one
        )
        created_vehicle = Vehicle.objects.get(pk="AB123CD")

        created_vehicle.owner = self.owner_two
        created_vehicle.save()

        vehicle = Vehicle.objects.get(pk="AB123CD")
        self.assertEqual(vehicle.owner, self.owner_two)

    def test_vehicle_creation_unique_license_plate(self):
        Vehicle.objects.create(
            license_plate="AB123CD", color="Red", brand="GM", owner=self.owner_one
        )
        with self.assertRaises(IntegrityError) as context:
            Vehicle.objects.create(
                license_plate="AB123CD",
                color="Blue",
                brand="Ford",
                owner=self.owner_two,
            )
        self.assertTrue("UNIQUE constraint failed" in str(context.exception))
