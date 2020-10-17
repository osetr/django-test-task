from django.shortcuts import render
from django.views.generic import View
from .models import Blog, Like
from posts.models import Post, Read
from django.http import Http404, JsonResponse


class ShowAllBlogs(View):
    """
        View to show all blogs.
    """

    def get(self, request):
        user_authenticated = request.user.is_authenticated
        blogs = Blog.objects.all()
        likes = Like.objects.filter(user=request.user)
        likes = [like.blog_id for like in likes]

        my_blog_id = Blog.objects.get(author=request.user).id

        return render(
            request,
            "all_blogs.html",
            context={
                "user_authenticated": user_authenticated,  # availability of site functionality
                "active_page": "all_blogs",  # separeate active and non active pages on navbar
                "blogs": blogs, # all blogs list 
                "likes": likes, # to highlight blogs, which user has liked 
                "my_blog_id": my_blog_id,
            },
        )


class ShowBlog(View):
    """
        View particular blog.
    """

    def get(self, request, pk):
        user_authenticated = request.user.is_authenticated
        posts = Post.objects.filter(blog_id=pk).all()
        likes_amount = Like.objects.filter(blog_id=pk).count()
        if int(pk) == Blog.objects.get(author=request.user).id:
            active_page = "my_blog"
            posts_owner = True
        else:
            active_page = "some_blog"
            posts_owner = False
        reads = Read.objects.filter(user=request.user)
        reads = [read.post_id for read in reads]

        my_blog_id = Blog.objects.get(author=request.user).id

        return render(
            request,
            "show_blog.html",
            context={
                "user_authenticated": user_authenticated,  # availability of site functionality
                "active_page": active_page,  # separeate active and non active pages on navbar
                "posts": posts, # just all posts from the blog
                "likes_amount": likes_amount, # show amount of likes into blog
                "posts_owner": posts_owner, # check is user is owner of blogs posts
                "reads": reads, # to highlight posts, which user has read
                "my_blog_id": my_blog_id,
            },
        )


def like_blog(request, pk):
    if request.is_ajax():
        blog = Blog.objects.get(pk=pk)
        try:
            Like.objects.get(blog_id=pk, user=request.user).delete()
            blog.likes -= 1
            blog.save()
            status = "Like removed"
        except Like.DoesNotExist:
            Like.objects.create(user=request.user, blog_id=pk)
            blog.likes += 1
            blog.save()
            status = "Like added"
        likes_amount = blog.likes
        response = {
            "likes_amount": likes_amount,
            "status": status,
            }
        return JsonResponse(response)
    else:
        raise Http404