from django.shortcuts import get_object_or_404
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from .models import Infraction
from vehicles.models import Vehicle



class InfractionSerializer(serializers.ModelSerializer):
    license_plate = serializers.CharField(max_length=30, read_only=True)

    class Meta:
        model = Infraction
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["officer"] = str(instance.officer)
        data["person"] = str(instance.person)
        data["vehicle"] = str(instance.vehicle)
        return data

    def validate_amount(self, value):
        if value < 0:
            raise serializers.ValidationError(
                _("Infraction amount value should be greater than 0.")
            )
        else:
            return value

    def validate(self, data):
        vehicle = get_object_or_404(Vehicle, pk=self.initial_data["license_plate"])
        self.initial_data["vehicle"] = self.initial_data["license_plate"]
        self.initial_data["person"] = vehicle.owner.id
        self.initial_data["officer"] = self.context["request"].user.officer.id
        return data
