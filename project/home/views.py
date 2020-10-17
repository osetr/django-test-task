from django.shortcuts import render
from django.views.generic import View
from blogs.models import Blog
from posts.models import Post, Read


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

            posts = (
                Post
                .objects
                .filter(blog__like__user=author)
                .order_by("date")
                .reverse()
            )
            reads = Read.objects.filter(user=request.user)
            reads = [read.post_id for read in reads]
            my_blog_id = Blog.objects.get(author=request.user).id
            try:
                Blog.objects.get(author=author)
            except Blog.DoesNotExist:
                Blog.objects.create(author=author)
        else:
            posts = ""
            reads = ""
            my_blog_id = ""

        return render(
            request,
            "home.html",
            context={
                "user_authenticated": user_authenticated,  # availability of site functionality
                "active_page": "home",  # separeate active and non active pages on navbar
                "posts": posts,  # all posts from blog, user subscribe to
                "posts_owner": False,  # as user cann't subscribe to his own blog
                "reads": reads,  # to highlight posts, which user has read
                "my_blog_id": my_blog_id,  # keep pk of personal blog for link in navbar
            },
        )
