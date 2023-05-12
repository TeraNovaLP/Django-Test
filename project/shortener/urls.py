from django.urls import path

from . import views

urlpatterns = [
    path("", views.shortener, name="index"),
    path("<int:id>", views.resolve),
]
