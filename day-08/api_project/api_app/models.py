from django.db import models


class OceanTide(models.Model):
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)

    description = models.CharField(max_length=10)
    inches = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Habitat(models.Model):
    name = models.CharField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Fish(models.Model):
    name = models.CharField()
    description = models.TextField()
    habitats = models.ManyToManyField(Habitat, related_name="fishes", blank=True)
    weight_in_lbs = models.DecimalField(decimal_places=2, max_digits=6)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)