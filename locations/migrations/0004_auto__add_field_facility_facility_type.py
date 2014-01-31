# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Facility.facility_type'
        db.add_column(u'locations_facility', 'facility_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sports.Facility_type'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Facility.facility_type'
        db.delete_column(u'locations_facility', 'facility_type_id')


    models = {
        u'locations.continent': {
            'Meta': {'object_name': 'Continent'},
            'continent': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'locations.country': {
            'Meta': {'object_name': 'Country'},
            'continent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.Continent']"}),
            'country': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'locations.facility': {
            'Meta': {'object_name': 'Facility'},
            'bookings_required': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2'}),
            'facility_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sports.Facility_type']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indoor_or_outdoor': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'lighting_at_night': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'members_only': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'number_of_these_facilities': ('django.db.models.fields.IntegerField', [], {}),
            'payment_required': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'saved': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'sports': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sports.Sport']"}),
            'surface': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sports.Surface_type']"}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.Venue']"})
        },
        u'locations.facilitypic': {
            'Meta': {'object_name': 'Facilitypic'},
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.Facility']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'saved': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'locations.state': {
            'Meta': {'object_name': 'State'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'locations.suburb': {
            'Meta': {'object_name': 'Suburb'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_code': ('django.db.models.fields.IntegerField', [], {}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.State']"}),
            'suburb': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'locations.venue': {
            'Meta': {'object_name': 'Venue'},
            'change_rooms': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50', 'blank': 'True'}),
            'friday_cl': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'friday_is_closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'friday_op': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monday_cl': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'monday_is_closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'monday_op': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'onsite_parking': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'phone_number': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'public_toilets': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'saturday_cl': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'saturday_is_closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'saturday_op': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'saved': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'street_address': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'suburb': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.Suburb']"}),
            'summary': ('django.db.models.fields.TextField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'sunday_cl': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'sunday_is_closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sunday_op': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'thursday_cl': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'thursday_is_closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'thursday_op': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'tuesday_cl': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'tuesday_is_closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tuesday_op': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True'}),
            'wednesday_cl': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'wednesday_is_closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wednesday_op': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'locations.venuepic': {
            'Meta': {'object_name': 'Venuepic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'saved': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.Venue']"})
        },
        u'sports.category': {
            'Meta': {'object_name': 'Category'},
            'category': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '70'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'sports.facility_type': {
            'Meta': {'object_name': 'Facility_type'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'sports.sport': {
            'Meta': {'object_name': 'Sport'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sports.Category']"}),
            'commonly_played_on_a': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sports.Facility_type']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'sports.surface_type': {
            'Meta': {'object_name': 'Surface_type'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'surface': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        }
    }

    complete_apps = ['locations']