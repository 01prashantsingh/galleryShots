from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("service/", views.service, name="Services"),
    path("gallery/", views.gallery, name="Gallery"),
   
]