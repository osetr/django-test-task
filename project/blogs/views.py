from django.shortcuts import render
from django.views.generic import View
from .models import Blog


class ShowAllBlogs(View):
    """
        View to show all blogs.
    """

    def get(self, request):
        user_authenticated = request.user.is_authenticated
        blogs = Blog.objects.all()

        return render(
            request,
            "all_blogs.html",
            context={
                "user_authenticated": user_authenticated,  # availability of site functionality
                "active_page": "all_blogs",  # separeate active and non active pages on navbar
                "blogs": blogs, # all blogs list 
            },
        )


class ShowBlog(View):
    """
        View particular blog.
    """

    def get(self, request, pk):
        user_authenticated = request.user.is_authenticated
        if int(pk) == request.user.id:
            active_page = "my_blog"
        else:
            active_page = "some_blog"

        return render(
            request,
            "home.html",
            context={
                "user_authenticated": user_authenticated,  # availability of site functionality
                "active_page": active_page,  # separeate active and non active pages on navbar
            },
        )

