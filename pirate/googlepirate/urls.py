from django.urls import re_path, path

from .views import acceptdialog


urlpatterns = [
    re_path(r'^$', acceptdialog, name='testing'),
]


