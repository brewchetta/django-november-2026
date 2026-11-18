from django.urls import path
from . import views

urlpatterns = [
    path('api/v1', views.welcome, name='welcome'),

    # GET ALL / POST
    path('api/v1/tides', views.ocean_tide_list, name="ocean_tide_list"),
    # GET ONE / PATCH / DELETE
    path('api/v1/tides/<int:pk>', views.ocean_tide_detail, name="ocean_tide_detail"),

    path('api/v1/habitats', views.HabitatList.as_view(), name="habitat_list"),

    path('api/v1/fish', views.FishListCreate.as_view(), name="fish_list_create"),
    path('api/v1/fish/<int:pk>', views.FishDetail.as_view(), name="fish_detail"),
]