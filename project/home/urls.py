from django.urls import path
from .views import HomeView


urlpatterns = [
    path(r"", HomeView.as_view(), name="home_v"),
    path(r"", HomeView.as_view(), name="sign_in_v"),
    path(r"", HomeView.as_view(), name="sign_up_v"),
]
