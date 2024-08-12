from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Officer(models.Model):
    badge = models.CharField(_("Badge number"), max_length=20, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.last_name}, {self.user.first_name} - {_('Badge number')}: {self.badge}"

    class Meta:
        verbose_name = _("Officer")
        verbose_name_plural = _("Officers")
