# this file to define what has to be sent to the user.

from django.shortcuts import render
from .models import Post


# --------------------------------------------------------------------------------------------
# basically this is the middleware to be
# passed while declaring the route.


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About!!'})
