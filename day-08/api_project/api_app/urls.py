from django.urls import path
from . import views

urlpatterns = [
    path('api/v1', views.welcome, name='welcome'),

    # GET / POST
    path('api/v1/tides', views.ocean_tide_list, name="ocean_tide_list"),
    # GET / PATCH / DELETE
    path('api/v1/tides/<int:id>', views.ocean_tide_detail, name="ocean_tide_detail")
]