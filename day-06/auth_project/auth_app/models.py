from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Music(models.Model):
    name = models.CharField()
    artist = models.CharField()
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING, related_name="submitted_music")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
