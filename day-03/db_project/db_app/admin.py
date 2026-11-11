from django.contrib import admin
from .models import WordDefinition, WordExample, Category

# Register your models here. You will now see them in the admin panel.
admin.site.register(WordDefinition)
admin.site.register(WordExample)
admin.site.register(Category)