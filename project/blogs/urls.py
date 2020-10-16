from django.urls import path
from .views import *


urlpatterns = [
    path(r"", ShowAllBlogs.as_view(), name="show_all_blogs_v"),
    path(r"blog/<pk>", ShowBlog.as_view(), name="show_blog_v"),
]
