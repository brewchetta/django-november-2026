from rest_framework import serializers
from .models import OceanTide

# a serializer allows us to shape the data and determine what the data looks like as we send it
class OceanTideSerializer(serializers.ModelSerializer):
    class Meta:
        model = OceanTide
        fields = ['id', 'lat', 'lon', 'description', 'inches', 'created_at']
        # fields determines what data we send and what gets omitted