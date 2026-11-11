from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('definitions/<int:id>', views.word_detail, name="word_detail"),
    path('definitions/<slug:word>', views.word_detail_by_slug, name="word_detail_by_slug"),
]