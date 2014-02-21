from django.db import models
from user_profile.models import Person
from teams.models import Group
from django import forms
from django.contrib.auth.models import User

class Leap(models.Model):
	message = models.CharField(max_length=500)
	author = models.ForeignKey(User)
	group = models.ForeignKey(Group)
	created_at = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
          return self.message


class leap_form(forms.Form):
	message = forms.CharField(widget = forms.Textarea,required=True)
	def save(self,group_obj,user_obj):
		new_leap = Leap(message=self.cleaned_data['message'],author=user_obj,group=group_obj)
		new_leap.save()
		return new_leap


	
