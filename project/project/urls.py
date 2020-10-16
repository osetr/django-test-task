from django.contrib import admin
from django.urls import path, include
from accounts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path("", include("accounts.urls")),
    path("blogs/", include("blogs.urls")),
    path("", include("home.urls")),
]
