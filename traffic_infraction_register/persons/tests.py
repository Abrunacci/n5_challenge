from copy import deepcopy
from django.db.utils import IntegrityError

from django.test import TestCase

from faker import Faker

# Create your tests here.
from .models import Person


faker = Faker()


class TestPerson(TestCase):

    def test_person_creation(self):

        person = {"full_name": faker.name(), "email": faker.email()}
        Person.objects.create(**person)

        created_person = Person.objects.get(email=person["email"])
        self.assertEqual(created_person.full_name, person["full_name"])
        self.assertEqual(created_person.email, person["email"])

    def test_person_creation_unique_email(self):
        person = {"full_name": faker.name(), "email": faker.email()}
        Person.objects.create(**person)
        other_person = deepcopy(person)
        other_person["full_name"] = faker.name()
        with self.assertRaises(IntegrityError) as context:
            Person.objects.create(**other_person)
        self.assertTrue("UNIQUE constraint failed" in str(context.exception))
