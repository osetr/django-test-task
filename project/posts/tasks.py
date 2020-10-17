from datetime import datetime, timedelta
from django.conf import settings
from celery.task import periodic_task
from django.core.mail import send_mail
from accounts.models import User
import requests
from posts.models import Post
from django.urls import reverse


@periodic_task(run_every=timedelta(seconds=10), name="send_info_about_new_post")
def send_info_about_new_post():
    try:
        post = Post.objects.filter(users_informed=False).first()
        users = User.objects.filter(like__blog__post=post)
        users = [user.email for user in users]
        subject = 'New post'
        message = (
            "You've got new post from blog, which you're subscribe to. \n" +
            "You can check it by link " + 
            settings.DOMAIN + 
            str(reverse('show_blog_v', args=(post.blog_id,)))
        )
        email_from = settings.EMAIL_HOST_USER
        recipient_list = users
        send_mail(subject, message, email_from, recipient_list)
        post.users_informed = True
        post.save()
        print("Celery just worked")
    except (Post.DoesNotExist, AttributeError):
        print("There is no any work for celery")