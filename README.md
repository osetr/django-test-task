# django-test-task
This project is a test-task for some company.

Description
===========

This is a little site, that include ability to create new posts for your own blog and look through other blogs. As long as you're not signed up, you cann't do anything on the site. But after first signing in, you'll get your own blog and you'll be able to add posts into it. Also each user can look through all blogs and add them to favourites(or like them, rate them, subscribe to them or whatever). Posts from liked blogs will appear on the home page. You can mark posts from blogs, which you've already read. If blogs owner add new post, subscribed users will receive message about this news, so that they couldn't miss new information.

Manual
======

As this project is dockerized, you can very quickly untap it on your machine. To do this, just clone this repo on your machine and up docker-compose. Also, don't forget to create a .env file in the root of the cloned directory and insert your key/value pairs in the following format of KEY=VALUE:

```sh
SECRET_KEY = 'key'
POSTGRES_USER = 'root'
POSTGRES_PASSWORD = 'pass'
POSTGRES_DB = 'project'
EMAIL_HOST_USER = 'email'
EMAIL_HOST_PASSWORD = 'emailpass'
```

Now, just check project at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Technology stack
================

In general, Django framework was used to create this site. [django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) module was used for authorization. It includes wide opportunities for developers. Bootstrap and vue.js are in charge of design(vue.js objects serve just for ajax requests). Celery needed to send messages, so that the site could do this in the background without overloading the server.
