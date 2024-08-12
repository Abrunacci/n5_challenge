from django.contrib import admin
from .models import Vehicle

# Register your models here.


class VehicleAdmin(admin.ModelAdmin):
    list_display = ("license_plate", "brand", "color", "owner__full_name")


admin.site.register(Vehicle, VehicleAdmin)
