from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
#from phone_field import PhoneField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_num = models.CharField(max_length=50,null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username


def save_profile_user(sender, **kwargs):
    if kwargs['created']:
        profile_user = Profile(user=kwargs['instance'])
        profile_user.save()


post_save.connect(save_profile_user, sender=User)


# class Location(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone_num = models.CharField(max_length=150,null=True, blank=True)
#     x = models.CharField(max_length=150, null=True, blank=True)
#     y = models.CharField(max_length=150, null=True, blank=True)
#
#     def __str__(self):
#         return self.user.username
#
#
# def save_location_user(sender, **kwargs):
#     if kwargs['created']:
#         location_user = Location(user=kwargs['instance'])
#         location_user.save()
#
#
# post_save.connect(save_location_user, sender=User)
