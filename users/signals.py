
# * this is a signal that gets fired, after an object is saved.
from django.db.models.signals import post_save

# * the user model here is going to be the sender.
from django.contrib.auth.models import User

# * this is the receiver. a receiver is a function that receives the signal and performs some task.
from django.dispatch import receiver

# * importing profiles from our models, since we'll be using profiles in our fucntion.
#  the reason we're importing is because we want to create a profile for each new user.
from .models import Profile

# the function explains that, when a receiver signal is received, with the post_save from the User;
# pass the params in the fucntion receoved from the User and check is user was created. If User was created,
# create a profile of that user using the Profile object imported earlier.


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
