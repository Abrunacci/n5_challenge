from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Person(models.Model):
    full_name = models.CharField(_("Person"), max_length=50)
    email = models.EmailField(_("Email"), unique=True)


    def __str__(self):
        return self.full_name