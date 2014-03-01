from user_profiles.models import UserProfile
from django import forms
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.models import User
from bootstrap3_datetime.widgets import DateTimePicker

class UserProfileForm(ModelForm):
	class Meta:
		model = UserProfile
		exclude = ['user']
		widgets = {
            'dob': DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": False}),
            'gender': forms.RadioSelect,
            'my_sports': forms.CheckboxSelectMultiple,
        }

class UserForm(ModelForm):
	class Meta:
		model = User
		fields=['username', 'first_name', 'last_name']

