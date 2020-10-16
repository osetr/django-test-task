from django.db import models
from datetime import datetime
from accounts.models import User


# keeps all blogs
class Blog(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, default="", editable=False
    )
    date = models.DateTimeField(default=datetime.now(), editable=False)
    likes = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return "blog by %s" % self.author