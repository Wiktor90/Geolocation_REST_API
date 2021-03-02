from rest_framework import serializers
from .models import Geodata


class GeodataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geodata
        fields = '__all__'
