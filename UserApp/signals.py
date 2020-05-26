from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from .models import Profile
from PlatformApp.models import Qualification


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='Student')
        instance.groups.add(group)
        Qualification.objects.create(user=instance, done_projects_count=0)
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
