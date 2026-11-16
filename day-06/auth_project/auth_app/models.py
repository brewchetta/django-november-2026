from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Music(models.Model):
    name = models.CharField()
    artist = models.CharField()
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING, related_name="submitted_music")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# extend the user with a profile model that has a 1:1 relationship with User
class Profile(models.Model):
    bio = models.TextField(blank=True, null=True)
    favorite_artist = models.CharField(blank=True, null=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")


from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kargs):
    if created:
        Profile.objects.create(user=instance)
