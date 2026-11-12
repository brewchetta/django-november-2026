from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100, unique=True)
    
    title_slug = models.SlugField(unique=True)
    
    runtime_in_minutes = models.IntegerField()
    
    director = models.CharField(max_length=100)
    
    release_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title