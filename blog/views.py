# this file to define what has to be sent to the user.

from django.shortcuts import render
from .models import Post
# this is a class based view.
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
# LoginRequiredMixin --> this package is for verifying whether the user is logged in or not.
# UserPassesTestMixin --> this package is for verifyign whether the user is the owner of the post while updating.
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# --------------------------------------------------------------------------------------------
# basically this is the middleware to be
# passed while declaring the route.


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    # this is to view our posts from newer -> older
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # so what this says is that, before you submit, set the instance.author to that current user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # so what this says is that, before you submit, set the instance.author to that current user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About!!'})
