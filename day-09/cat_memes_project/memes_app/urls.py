from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.memes_index, name="memes_index"),
    path('memes/create', views.memes_create, name="memes_create"),
]

# in debug mode we are building paths for our images as though they were static files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)