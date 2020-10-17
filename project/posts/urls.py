from django.urls import path
from .views import *


urlpatterns = [
    path(r"post/new", AddNewPostView.as_view(), name="add_post_v"),
    path(r"ajax/read_post/", read_post, name="read_post_ajax_v"),
    path(r"ajax/read_post/<pk>", read_post, name="read_post_ajax_v"),
]
