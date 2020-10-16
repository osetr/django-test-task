from django.urls import path
from .views import *


urlpatterns = [
    path(r"post/new", AddNewPostView.as_view(), name="add_post_v"),
]
