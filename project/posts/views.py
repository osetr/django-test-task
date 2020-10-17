from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Post, Read
from accounts.models import User
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

        return render(
            request,
            "add_post.html",
            context={
                "form": form, # just form on the page
                "user_authenticated": user_authenticated,  # adjust navbar functions
            },
        )

    def post(self, request):
        form = AddPostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.blog = Blog.objects.get(author_id=request.user.id)
            post.save()
        return redirect("show_blog_v", pk=request.user.id)


def read_post(request, pk):
    if request.is_ajax():
        post = Post.objects.get(pk=pk)
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