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


class Character(models.Model):
    name = models.CharField(max_length=100)
    actor = models.CharField(max_length=100)

    def name_slug(self):
        return self.name.lower().replace(" ", "-")

    # ForeignKey is for one to many relationship
    # character belongs to a movie
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="characters")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)