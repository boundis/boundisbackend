from models import Leap
from django import forms
from django.contrib.auth.models import User

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
