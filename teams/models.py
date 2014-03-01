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

class group_form(forms.Form):
	group_name = forms.CharField(required=True)
	group_type = forms.ChoiceField(widget=forms.Select, choices=GROUP_CHOICES)
	def save(self,person_obj):
		new_group = Group(group_name=self.cleaned_data['group_name'],group_type=self.cleaned_data['group_type'])
		new_group.save()
		new_membership = Membership(person=person_obj,membership_type='owner',group=new_group)
		new_membership.save()
		return new_group
		
class add_member_form(forms.Form):
	member = forms.CharField(required=True)
	membership_type = forms.ChoiceField(widget=forms.Select, choices=MEMBERSHIP_CHOICES)
	def save(self,group_obj):
		try:
			persons = User.objects.get(username=self.cleaned_data['member'])
		except User.DoesNotExist:
			return "User does not exist."
		personss = User.objects.get(username=persons)
		try:
			check = Membership.objects.get(group=group_obj,person=personss)
			return "User already in group"
		except Membership.DoesNotExist:
			new_membership = Membership(person=personss,membership_type=self.cleaned_data['membership_type'],group=group_obj)
			new_membership.save()
			return new_membership


			
		