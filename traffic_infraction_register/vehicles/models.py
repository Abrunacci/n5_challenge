from django.db import models
from django.utils.translation import gettext_lazy as _
from persons.models import Person


# Create your models here.
class Vehicle(models.Model):
    license_plate = models.CharField(_("License Plate"), max_length=10, unique=True)
    brand = models.CharField(_("Brand"), max_length=20)
    color = models.CharField(_("Color"), max_length=15)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='vehicles')

    class Meta:
        verbose_name = _("Vehicle")
        verbose_name_plural = _("Vehicles")