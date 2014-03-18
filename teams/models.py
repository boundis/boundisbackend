from django.db import models
from django import forms
from user_profiles.models import UserProfile
from django.contrib.auth.models import User

GROUP_CHOICES = (
        ('team', 'Team'),
        ('club', 'Club'),
        ('organisation', 'Organisation'),
		)
MEMBERSHIP_CHOICES = (('owner','Owner'),('member','Member'),)
class Group(models.Model):
    group_name = models.CharField(max_length=100)
    group_type = models.CharField(choices=GROUP_CHOICES, max_length=100)
    members = models.ManyToManyField(User, through='Membership')
    def __unicode__(self):
          return self.group_name

class Membership(models.Model):
	person = models.ForeignKey(User)
	membership_type = models.CharField(choices=MEMBERSHIP_CHOICES, max_length=20)
	group = models.ForeignKey(Group)
	date_joined = models.DateField(auto_now=True)
	def __unicode__(self):
		return self.group.group_name + ' Adding: ' + self.person.username + ' as ' + self.membership_type
