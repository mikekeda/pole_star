from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
    path("", include("ships.urls", namespace="ships")),
    path("admin/", admin.site.urls),
]

admin.site.site_header = _("Pole star")
