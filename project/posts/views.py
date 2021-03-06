from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Read
from blogs.models import Blog
from .forms import AddPostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, JsonResponse


class AddNewPostView(LoginRequiredMixin, View):
    """
        View for adding new posts
    """

    login_url = "/sign_in/"

    def get(self, request):
        user_authenticated = request.user.is_authenticated
        form = AddPostForm(request.POST)
        my_blog_id = Blog.objects.get(author=request.user).id

        return render(
            request,
            "add_post.html",
            context={
                "form": form,  # just form on the page
                "user_authenticated": user_authenticated,  # adjust navbar functions
                "my_blog_id": my_blog_id,  # keep pk of personal blog for link in navbar
            },
        )

    def post(self, request):
        form = AddPostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.blog = Blog.objects.get(author_id=request.user.id)
            post.save()
            return redirect("show_blog_v", pk=post.blog.id)


def read_post(request, pk):
    if request.is_ajax():
        try:
            Read.objects.get(post_id=pk).delete()
            status = "Read removed"
        except Read.DoesNotExist:
            Read.objects.create(user=request.user, post_id=pk)
            status = "Read added"
        response = {
            "status": status,
        }
        return JsonResponse(response)
    else:
        raise Http404
