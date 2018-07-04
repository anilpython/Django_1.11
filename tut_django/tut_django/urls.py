from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^webapp/',include('webapp.urls')),
    url(r'^items/',include('menus.urls',namespace="menus")),
    url(r'^api/',include('api.urls',namespace="api")),
    url(r'^admin/', admin.site.urls),
]
