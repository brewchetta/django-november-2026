from django.db import models


class CatMeme(models.Model):
    title = models.CharField()

    # ImageField links to an image file either on the computer or the cloud
    # upload_to will be a special subfolder for these images
    image = models.ImageField(upload_to="meme_imgs")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)