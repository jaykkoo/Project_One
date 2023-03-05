
from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home",),
    path("about-us", about_us, name="about-us",),
    path("contact-us", contact_us, name="contact-us",),
    path("login", login, name="login")
]