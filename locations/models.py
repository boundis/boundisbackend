from django.db import models
from time import time
import os


# Create your models here.
class Continent(models.Model):
	continent = models.CharField(max_length=100, unique=True)

	def __unicode__(self):
		return self.continent 

class Country(models.Model):
	country= models.CharField(max_length=100, unique=True)
	continent = models.ForeignKey(Continent)

	def __unicode__(self):
		return self.country
	class Meta:
    		verbose_name_plural = 'Countries'

class State(models.Model):
	state= models.CharField(max_length=100)
	abbreviation = models.CharField(max_length=5, null=True)
	country= models.ForeignKey(Country)

	def __unicode__(self):
		return self.state

class Suburb(models.Model):
	suburb = models.CharField(max_length=50)
	state = models.ForeignKey(State)
	post_code = models.IntegerField()

	def __unicode__(self):
		return "%s, %i" %(self.suburb, self.post_code)
	def country(object):
  		return object.state.country


class Venue(models.Model):
	name = models.CharField(max_length=60)
	suburb = models.ForeignKey(Suburb)
	street_address = models.CharField(max_length=60)
	phone_number = models.IntegerField()
	email = models.EmailField(max_length=50)
	website = models.CharField(max_length=150, null=True)
	is_choices=(('yes', 'Yes'), ('no', 'No'))
	public_toilets = models.CharField(choices=is_choices, max_length=3)
	change_rooms = models.CharField(choices=is_choices, max_length=3)
	onsite_parking = models.CharField(choices=is_choices, max_length=3)
	summary = models.TextField(max_length=120)
	monday_op = models.TimeField(blank=True, null=True)
	monday_cl = models.TimeField(blank=True, null=True)
	monday_is_closed = models.BooleanField(default=False)
	tuesday_op = models.TimeField(blank=True, null=True)
	tuesday_cl = models.TimeField(blank=True, null=True)
	tuesday_is_closed = models.BooleanField(default=False)
	wednesday_op = models.TimeField(blank=True, null=True)
	wednesday_cl = models.TimeField(blank=True, null=True)
	wednesday_is_closed = models.BooleanField(default=False)
	thursday_op = models.TimeField(blank=True, null=True)
	thursday_cl = models.TimeField(blank=True, null=True)
	thursday_is_closed = models.BooleanField(default=False)
	friday_op = models.TimeField(blank=True, null=True)
	friday_cl = models.TimeField(blank=True, null=True)
	friday_is_closed = models.BooleanField(default=False)
	saturday_op = models.TimeField(blank=True, null=True)
	saturday_cl = models.TimeField(blank=True, null=True)
	saturday_is_closed = models.BooleanField(default=False)
	sunday_op = models.TimeField(blank=True, null=True)
	sunday_cl = models.TimeField(blank=True, null=True)
	sunday_is_closed = models.BooleanField(default=False)
	#creator = models.ForeignKey(User)
	saved = models.DateTimeField(auto_now_add=True)
	#last_edited_by = models.ForeignKey(User)
	#last_edited = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.name
		return self.street_address
		return self.suburb
	def state(object):
  		return object.suburb.state
	def country(object):
  		return object.suburb.state.country

def venue_upload_path(instance, filename):
	return os.path.join("venue",
      "%s_%i" %(instance.venue.name, instance.venue.id), "images", filename)

class Venuepic(models.Model):
	venue = models.ForeignKey(Venue)
	image = models.ImageField(upload_to=venue_upload_path)
	saved = models.DateTimeField(auto_now_add=True)
	#uploaded_by = models.ForeignKey(User)
	def __unicode__(self):
		return self.image

class Facility(models.Model):
	venue = models.ForeignKey(Venue)
	sports = models.ForeignKey('sports.Sport')
	facility_type = models.ForeignKey('sports.Facility_type', default=1)
	surface = models.ForeignKey('sports.Surface_type')
	number_of_these_facilities = models.IntegerField()
	is_choices=(('yes', 'Yes'), ('no', 'No'))
	members_only = models.CharField(choices=is_choices, max_length=3)
	payment_required = models.CharField(choices=is_choices, max_length=3)
	cost = models.DecimalField(max_digits=6, decimal_places=2, null=True)
	bookings_required = models.CharField(choices=is_choices, max_length=3)
	indoor_or_outdoor_choices=(('indoor', 'Indoor'), ('outdoor', 'Outdoor'), ('both', 'Both'))
	indoor_or_outdoor = models.CharField(choices=indoor_or_outdoor_choices, max_length=7)
	lighting_at_night= models.CharField(choices=is_choices, max_length=3)
	#creator = models.ForeignKey(User)
	saved = models.DateTimeField(auto_now_add=True)
	#last_edited_by = models.ForeignKey(User)
	#last_edited = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return "%s, %s" %(self.venue, self.sports)
		return self.sports.name
		return self.facility_type.name
	class Meta:
    		unique_together = ('venue', 'sports',)
    		verbose_name_plural = 'Facilities'

def facility_upload_path(instance, filename):
	return os.path.join("venue",
      "%s_%i" %(instance.facility.venue, instance.facility.venue.id), "images",filename)

class Facilitypic(models.Model):
	facility= models.ForeignKey(Facility)
	image = models.ImageField(upload_to=facility_upload_path)
	saved = models.DateTimeField(auto_now_add=True)
	#uploaded_by = models.ForeignKey(User)













