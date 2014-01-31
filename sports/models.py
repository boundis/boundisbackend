from django.db import models
import os

class Category(models.Model):
    category = models.CharField(max_length=30, unique=True, blank=False)
    description = models.TextField(max_length=70, blank=False)
    def __unicode__(self):
          return self.category
    class Meta:
          verbose_name_plural = 'Categories'

class Facility_type(models.Model):
	name = (models.CharField(max_length=20))
	def __unicode__(self):
		return self.name

class Surface_type(models.Model):
    surface = models.CharField(max_length=20, unique=True, blank=False)
    def __unicode__(self):
        return self.surface

def sport_upload_path(instance, filename):
    return os.path.join("sport",
      "%s" %(instance.name), "images", filename)

class Sport(models.Model):
    name = models.CharField(max_length=30, unique=True)
    category = models.ForeignKey(Category)
    commonly_played_on_a = models.ForeignKey(Facility_type)
    image = models.ImageField(upload_to=sport_upload_path, null=True)
    def __unicode__(self):
          return self.name

def sport_upload_path(instance, filename):
    return os.path.join("sport",
      "%s_%i" %(instance.sport.name), "images", filename)


