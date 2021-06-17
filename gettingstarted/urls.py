from django.contrib import admin
from django.conf.urls import include, url
from django.urls import include, path

admin.autodiscover()

import ifp
import tools_for_change
import hello

urlpatterns = [
    path('', include('ifp.urls')),
    path('ifp/', include('ifp.urls')),
    path('tfc/', include('tools_for_change.urls')),

    path("hello/", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),

    path("admin/", admin.site.urls),
]
