from django.contrib import admin
from django.urls import path
from django.conf.urls import include, re_path
from googlepirate.urls import urlpatterns


urlpatterns = [

    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('admin/', admin.site.urls),
    re_path(r'^$', include('googlepirate.urls')),
]
