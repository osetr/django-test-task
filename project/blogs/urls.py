from django.urls import path
from .views import *


urlpatterns = [
    path(r"", ShowAllBlogs.as_view(), name="show_all_blogs_v"),
    path(r"blog/<pk>", ShowBlog.as_view(), name="show_blog_v"),
    path(r"ajax/like_blog/", like_blog, name="like_blog_ajax_v"),
    path(r"ajax/like_blog/<pk>", like_blog, name="like_blog_ajax_v"),
]
