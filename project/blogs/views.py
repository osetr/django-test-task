from django.shortcuts import render
from django.views.generic import View


class ShowAllBlogs(View):
    """
        View to show all blogs.
    """

    def get(self, request):
        user_authenticated = request.user.is_authenticated

        return render(
            request,
            "home.html",
            context={
                "user_authenticated": user_authenticated,  # availability of site functionality
                "active_page": "all_blogs",  # separeate active and non active pages on navbar
            },
        )


class ShowBlog(View):
    """
        View particular blog.
    """

    def get(self, request):
        user_authenticated = request.user.is_authenticated
        if True:
            active_page = "my_blog"

        return render(
            request,
            "home.html",
            context={
                "user_authenticated": user_authenticated,  # availability of site functionality
                "active_page": active_page,  # separeate active and non active pages on navbar
            },
        )

