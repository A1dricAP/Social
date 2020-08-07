# file to map the  urls to the corresponding function in view.

from . import views  # importing the view from views file in blog.
from django.urls import path

# this url patterns is important; just like defining routes in javascript.
urlpatterns = [
    # importing the home view from view file to run on the default route, with the name: blog-home
    path('', views.home, name='blog-home')
]
