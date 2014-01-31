from locations import models
from django import forms
from django.forms import ModelForm


class venue_form(ModelForm):
	class Meta:
		model = models.Venue

class add_facility_form(ModelForm):
	class Meta:
		model = models.Facility
		exclude = ['venue']

class venuepic_form(ModelForm):
	class Meta:
		model = models.Venuepic
		exclude = ['venue']

class facilitypic_form(ModelForm):
	class Meta:
		model = models.Facilitypic
		exclude = ['facility']

