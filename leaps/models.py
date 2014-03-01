from django.db import models
from user_profiles.models import UserProfile
from teams.models import Group
from bugger.models import Bug
from django import forms
from django.contrib.auth.models import User

class Leap(models.Model):
	message = models.CharField(max_length=500)
	author = models.ForeignKey(User)
	group = models.ForeignKey(Group, related_name='group_leap_to',blank=True,null=True)
	bug = models.ForeignKey(Bug, related_name='bug_leap_to',blank=True,null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
          return self.message


class leap_form(forms.Form):
	message = forms.CharField(widget = forms.Textarea,required=True)
	def save(self,group_obj,user_obj):
		new_leap = Leap(message=self.cleaned_data['message'],author=user_obj,group=group_obj)
		new_leap.save()
		return new_leap

class leap_form_bug(forms.Form):
        message = forms.CharField(widget = forms.Textarea,required=True)
        def save(self,bug_obj,user_obj):
                new_leap = Leap(message=self.cleaned_data['message'],author=user_obj,bug=bug_obj)
                new_leap.save()
                return new_leap

	
