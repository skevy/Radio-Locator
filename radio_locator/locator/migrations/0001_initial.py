# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'StationMySQL'
        db.create_table(u'station', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('frequency', self.gf('django.db.models.fields.FloatField')()),
            ('call_letters', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('format', self.gf('django.db.models.fields.CharField')(max_length=90)),
            ('latitude_degrees', self.gf('django.db.models.fields.IntegerField')()),
            ('latitude_minutes', self.gf('django.db.models.fields.IntegerField')()),
            ('latitude_seconds', self.gf('django.db.models.fields.IntegerField')()),
            ('longitude_degrees', self.gf('django.db.models.fields.IntegerField')()),
            ('longitude_minutes', self.gf('django.db.models.fields.IntegerField')()),
            ('longitude_seconds', self.gf('django.db.models.fields.IntegerField')()),
            ('local_range', self.gf('django.db.models.fields.FloatField')()),
            ('distant_range', self.gf('django.db.models.fields.FloatField')()),
            ('fringe_range', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('locator', ['StationMySQL'])

        # Adding model 'Station'
        db.create_table('locator_station', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('frequency', self.gf('django.db.models.fields.FloatField')()),
            ('call_letters', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('format', self.gf('django.db.models.fields.CharField')(max_length=90)),
            ('location', self.gf('django.contrib.gis.db.models.fields.PointField')(blank=True)),
            ('local_range', self.gf('django.db.models.fields.FloatField')()),
            ('distant_range', self.gf('django.db.models.fields.FloatField')()),
            ('fringe_range', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('locator', ['Station'])


    def backwards(self, orm):
        
        # Deleting model 'StationMySQL'
        db.delete_table(u'station')

        # Deleting model 'Station'
        db.delete_table('locator_station')


    models = {
        'locator.station': {
            'Meta': {'object_name': 'Station'},
            'call_letters': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'distant_range': ('django.db.models.fields.FloatField', [], {}),
            'format': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'frequency': ('django.db.models.fields.FloatField', [], {}),
            'fringe_range': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local_range': ('django.db.models.fields.FloatField', [], {}),
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
