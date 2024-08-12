from django.db import models
from officers.models import Officer
from persons.models import Person
from vehicles.models import Vehicle


# Create your models here.
class Infraction(models.Model):
    officer = models.ForeignKey(
        Officer, on_delete=models.CASCADE, related_name="infractions_delivered"
    )
    person = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name="infractions_received"
    )
    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.CASCADE, related_name="infractions"
    )
    date = models.DateField()
    type = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"[{self.date}][{self.vehicle}]{self.type}: {self.description}"
