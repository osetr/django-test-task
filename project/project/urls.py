from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r"admin/", admin.site.urls),
    path(r"accounts/", include("allauth.urls")),
    path(r"", include("accounts.urls")),
    path(r"", include("home.urls")),
    path(r"blogs/", include("blogs.urls")),
    path(r"posts/", include("posts.urls")),
]
