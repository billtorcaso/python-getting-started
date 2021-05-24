from django.contrib import admin
from django.conf.urls import include, url
from django.urls import include, path

admin.autodiscover()

import ifp
import tools_for_change
import hello

urlpatterns = [

    #### This is old-think
    ###path("hello/", include("hello.urls")),
    ###path("db/", include("hello.urls")),

    path('', include('ifp.urls')),
    path('ifp/', include('ifp.urls')),
    path('tfc/', include('tools_for_change.urls')),
    path("admin/", admin.site.urls),
]
