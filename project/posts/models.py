from django.db import models
from datetime import datetime
from blogs.models import Blog
from accounts.models import User


# keeps all posts
class Post(models.Model):
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        default="",
        editable=False
    )
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=4024, blank=True)
    date = models.DateTimeField(default=datetime.now(), editable=False)
    users_informed = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return "post from %s by %s" % (self.title, self.blog.author)


class Read(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default="",
        editable=False
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        default="",
        editable=False
    )

    def __str__(self):
        return "user  %s" % self.user
