from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("applications/", include("jobApplications.urls")),
    path("admin/", admin.site.urls),
]