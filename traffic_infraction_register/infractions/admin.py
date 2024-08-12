from django.contrib import admin
from .models import Infraction


class InfractionAdmin(admin.ModelAdmin):
    list_display = (
        "vehicle__license_plate",
        "officer__badge",
        "type",
        "date",
        "amount",
    )
    search_fields = (
        "person__email",
        "vehicle__license_plate",
        "type",
        "officer__badge",
    )
    list_filter = ("type", "date")


admin.site.register(Infraction, InfractionAdmin)
