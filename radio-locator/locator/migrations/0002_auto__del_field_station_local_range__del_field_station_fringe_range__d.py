# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Station.local_range'
        db.delete_column('locator_station', 'local_range')

        # Deleting field 'Station.fringe_range'
        db.delete_column('locator_station', 'fringe_range')

        # Deleting field 'Station.distant_range'
        db.delete_column('locator_station', 'distant_range')

        # Adding field 'Station.local_range_val'
        db.add_column('locator_station', 'local_range_val', self.gf('django.db.models.fields.FloatField')(default=''), keep_default=False)

        # Adding field 'Station.distant_range_val'
        db.add_column('locator_station', 'distant_range_val', self.gf('django.db.models.fields.FloatField')(default=''), keep_default=False)

        # Adding field 'Station.fringe_range_val'
        db.add_column('locator_station', 'fringe_range_val', self.gf('django.db.models.fields.FloatField')(default=''), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Station.local_range'
        db.add_column('locator_station', 'local_range', self.gf('django.db.models.fields.FloatField')(default=''), keep_default=False)

        # Adding field 'Station.fringe_range'
        db.add_column('locator_station', 'fringe_range', self.gf('django.db.models.fields.FloatField')(default=''), keep_default=False)

        # Adding field 'Station.distant_range'
        db.add_column('locator_station', 'distant_range', self.gf('django.db.models.fields.FloatField')(default=''), keep_default=False)

        # Deleting field 'Station.local_range_val'
        db.delete_column('locator_station', 'local_range_val')

        # Deleting field 'Station.distant_range_val'
        db.delete_column('locator_station', 'distant_range_val')

        # Deleting field 'Station.fringe_range_val'
        db.delete_column('locator_station', 'fringe_range_val')


    models = {
        'locator.station': {
            'Meta': {'object_name': 'Station'},
            'call_letters': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'distant_range_val': ('django.db.models.fields.FloatField', [], {}),
            'format': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'frequency': ('django.db.models.fields.FloatField', [], {}),
            'fringe_range_val': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local_range_val': ('django.db.models.fields.FloatField', [], {}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'locator.stationmysql': {
            'Meta': {'object_name': 'StationMySQL', 'db_table': "u'station'"},
            'call_letters': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'distant_range': ('django.db.models.fields.FloatField', [], {}),
            'format': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'frequency': ('django.db.models.fields.FloatField', [], {}),
            'fringe_range': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'latitude_degrees': ('django.db.models.fields.IntegerField', [], {}),
            'latitude_minutes': ('django.db.models.fields.IntegerField', [], {}),
            'latitude_seconds': ('django.db.models.fields.IntegerField', [], {}),
            'local_range': ('django.db.models.fields.FloatField', [], {}),
            'longitude_degrees': ('django.db.models.fields.IntegerField', [], {}),
            'longitude_minutes': ('django.db.models.fields.IntegerField', [], {}),
            'longitude_seconds': ('django.db.models.fields.IntegerField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['locator']
