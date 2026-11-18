from rest_framework import serializers
from .models import OceanTide, Fish, Habitat

# a serializer allows us to shape the data and determine what the data looks like as we send it
class OceanTideSerializer(serializers.ModelSerializer):
    class Meta:
        model = OceanTide
        fields = ['id', 'lat', 'lon', 'description', 'inches', 'created_at']
        # fields determines what data we send and what gets omitted


class FishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fish
        fields = '__all__'

    # to_representation is what happens under the hood when converting to a dict
    def to_representation(self, instance):
        # start with the original to_representation
        data = super().to_representation(instance)
        # edit how habitats look and work
        data['habitats'] = FishHabitatSerializer(instance.habitats.all(), many=True).data
        # return the new populated version
        return data


class HabitatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitat
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['fishes'] = HabitatFishSerializer(instance.fishes.all(), many=True).data
        return data


# special serializers that allow us to grab a model without grabbing their associations
# this prevents an infinite loop in the serializers up above

class HabitatFishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fish
        exclude = ['habitats']

class FishHabitatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitat
        fields = '__all__'