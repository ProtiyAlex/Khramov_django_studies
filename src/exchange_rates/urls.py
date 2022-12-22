from django.urls import path

from .api import get_convert

urlpatterns = [
    path("convert/", get_convert, name="get_convert"),
]
