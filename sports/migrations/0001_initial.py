# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'sports_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=70)),
        ))
        db.send_create_signal(u'sports', ['Category'])

        # Adding model 'Facility_type'
        db.create_table(u'sports_facility_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'sports', ['Facility_type'])

        # Adding model 'Surface'
        db.create_table(u'sports_surface', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('surface', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
        ))
        db.send_create_signal(u'sports', ['Surface'])

        # Adding model 'Sport'
        db.create_table(u'sports_sport', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sports.Category'])),
            ('commonly_played_on_a', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sports.Facility_type'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True)),
        ))
        db.send_create_signal(u'sports', ['Sport'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'sports_category')

        # Deleting model 'Facility_type'
        db.delete_table(u'sports_facility_type')

        # Deleting model 'Surface'
        db.delete_table(u'sports_surface')

        # Deleting model 'Sport'
        db.delete_table(u'sports_sport')


    models = {
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
        u'sports.surface': {
            'Meta': {'object_name': 'Surface'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'surface': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        }
    }

    complete_apps = ['sports']