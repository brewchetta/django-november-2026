from django.urls import path

# import all views from views.py
from . import views

urlpatterns = [
    # two routes:

    # home route - "/"
    path('', views.home, name="home"),
    # about route - "/about"
    path('about', views.about, name="about"),
    # context route - "/context"
    path('context', views.context, name="context"),
    # contacts route - "/contacts"
    path('contacts', views.contacts, name="contacts"),
]

# adding new pages
# 1. add a path to urlpatterns
# 2. add a new view
# 3. add a new template under /templates