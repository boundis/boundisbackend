from django.db import models
from django import forms
from sports.models import Sport
from django.contrib.auth.models import User
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.models import Group
import os

def profile_pic_upload_path(instance, filename):
	return os.path.join("user",
      "%s" %(instance.user.username), "images", filename)

class Person(models.Model):
    user = models.OneToOneField(User)
    sex = models.CharField(max_length=8)
    dob = models.DateField()
    sport_intention = models.ManyToManyField(Sport)
    profile_pic= models.ImageField(upload_to=profile_pic_upload_path, blank=True)
    def __unicode__(self):
        return self.user.last_name + ', ' + self.user.first_name
		

class user_form(forms.Form):
	choices = [(b.id, b.name) for b in Sport.objects.all()]
	sex_choices = (('male', 'Male'),('female', 'Female'))
	username = forms.CharField(max_length=30,required=True)
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	password1=forms.CharField(max_length=100,widget=forms.PasswordInput())
	password2=forms.CharField(max_length=100,widget=forms.PasswordInput())
	email=forms.EmailField(required=True)
	sex = forms.CharField(widget=forms.RadioSelect(choices=sex_choices),required=True)
	intentions = forms.MultipleChoiceField(widget=forms.SelectMultiple,label="Intentions",choices=choices)
	dob = forms.DateField(widget=SelectDateWidget(years=range(1910, 2015)))
	profile_pic = forms.ImageField(required=False)
	def save(self): # create new user
		new_user=User.objects.create_user(self.cleaned_data['username'].lower(),
		                                  self.cleaned_data['email'],
		                                  self.cleaned_data['password1'])
		new_user.first_name = self.cleaned_data['first_name']
		new_user.last_name = self.cleaned_data['last_name']
		new_user.save()
		g = Group.objects.get(name='site_user')
		g.user_set.add(new_user)
		new_person = Person(user=new_user,sex=self.cleaned_data['sex'],dob=self.cleaned_data['dob'], profile_pic=self.cleaned_data['profile_pic'],)
		new_person.save()
		new_person.sport_intention = self.cleaned_data['intentions']
		new_person.save()
		return new_person
