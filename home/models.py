# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Photo(models.Model):

    #__Photo_FIELDS__
    asdf = models.CharField(max_length=255, null=True, blank=True)

    #__Photo_FIELDS__END

    class Meta:
        verbose_name        = _("Photo")
        verbose_name_plural = _("Photo")


class Another(models.Model):

    #__Another_FIELDS__

    #__Another_FIELDS__END

    class Meta:
        verbose_name        = _("Another")
        verbose_name_plural = _("Another")



#__MODELS__END
