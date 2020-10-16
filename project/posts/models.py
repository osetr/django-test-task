from django.db import models
from datetime import datetime
from blogs.models import Blog


# keeps all posts
class Post(models.Model):
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, default="", editable=False
    )
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=4024, blank=True)
    date = models.DateTimeField(default=datetime.now(), editable=False)


    def __str__(self):
        return "post from %s by %s" % (self.title, self.blog.author)