from django.shortcuts import render
from django.views.generic import View
from blogs.models import Blog


class HomeView(View):
    """
        View to show introductory page.
    """

    def get(self, request):
        user_authenticated = request.user.is_authenticated

        # create blog if user still doesn't have it
        # user already has his own blog, cause
        # after signing in user is redirected to this view
        # therefore, for sure, blog will be created
        if user_authenticated:
            author = request.user
            try:
                Blog.objects.get(author=author)
            except Blog.DoesNotExist:
                Blog.objects.create(author=author)

        return render(
            request,
            "home.html",
            context={
                "user_authenticated": user_authenticated,  # availability of site functionality
                "active_page": "home",  # separeate active and non active pages on navbar
            },
        )
