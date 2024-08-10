from typing import Any
from django.contrib import admin
from .models import Officer
from .forms import OfficerForm
from django.utils.translation import gettext_lazy as _


# Register your models here.
class OfficerAdmin(admin.ModelAdmin):
    form = OfficerForm
    list_display = ("last_name", "first_name", "badge")

    def last_name(self, obj):
        return obj.user.last_name

    def first_name(self, obj):
        return obj.user.first_name

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        form.save(commit=True)
        super().save_model(request, obj, form, change)

    first_name.short_description = _("First Name")
    last_name.short_description = _("Last Name")


admin.site.register(Officer, OfficerAdmin)