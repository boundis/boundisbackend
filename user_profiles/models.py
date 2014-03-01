from django.contrib.auth.models import User
from django.db import models
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount
from locations.models import Suburb
from sports.models import Sport

import hashlib


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    gender_choices = (('male', 'Male'),('female', 'Female'))
    gender = models.CharField(choices=gender_choices, max_length=8, default='male')
    dob = models.DateField(blank=True, null=True, verbose_name='Date of Birth')
    my_sports = models.ManyToManyField(Sport)

    def __unicode__(self):
        return "{}'s profile".format(self.user.username)

    class Meta:
        db_table = 'user_profile'

    def profile_image_url(self):
        """
        Return the URL for the user's Facebook icon if the user is logged in via Facebook,
        otherwise return the user's Gravatar URL
        """
        fb_uid = SocialAccount.objects.filter(user_id=self.user.id, provider='facebook')

        if len(fb_uid):
            return "http://graph.facebook.com/{}/picture?width=75&height=75".format(fb_uid[0].uid)

        return "/media/site_images/blank-avatar.jpg"
    def profile_image_sm_url(self):
        """
        Return the URL for the user's Facebook icon if the user is logged in via Facebook,
        otherwise return the user's Gravatar URL
        """
        fb_uid = SocialAccount.objects.filter(user_id=self.user.id, provider='facebook')

        if len(fb_uid):
            return "http://graph.facebook.com/{}/picture?width=5&height=6".format(fb_uid[0].uid)

        return "/media/site_images/blank-avatar-sm.jpg"

    def account_verified(self):
        """
        If the user is logged in and has verified hisser email address, return True,
        otherwise return False
        """
        if self.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.user.email)
            if len(result):
                return result[0].verified
        return False


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


