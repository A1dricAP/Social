from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Post(models.Model):  # creating the following attributes.

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

# this function is created to present the title of this post as the Post reference in the sql python terminal
    def __str__(self):
        return self.title

# this function is basically to redirect me to the post-detail page after creating a new post.
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
