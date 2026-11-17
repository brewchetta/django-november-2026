from django.db import models


class VideoGame(models.Model):
    title = models.CharField()
    description = models.TextField()
    genre = models.CharField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)