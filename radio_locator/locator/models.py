from django.db import models as normal_models

from django.contrib.gis.db import models

class StationMySQL(normal_models.Model):
    id = models.IntegerField(primary_key=True)
    frequency = models.FloatField()
    call_letters = models.CharField(max_length=30)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=60)
    format = models.CharField(max_length=90)
    latitude_degrees = models.IntegerField()
    latitude_minutes = models.IntegerField()
    latitude_seconds = models.IntegerField()
    longitude_degrees = models.IntegerField()
    longitude_minutes = models.IntegerField()
    longitude_seconds = models.IntegerField()
    local_range = models.FloatField()
    distant_range = models.FloatField()
    fringe_range = models.FloatField()
    class Meta:
        db_table = u'station'
        
class Station(models.Model):
    frequency = models.FloatField()
    call_letters = models.CharField(max_length=30)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=60)
    format = models.CharField(max_length=90)
    location = models.PointField(blank=True)
    local_range = models.PolygonField()
    distant_range = models.PolygonField()
    fringe_range = models.PolygonField()
    local_range_val = models.FloatField()
    distant_range_val = models.FloatField()
    fringe_range_val = models.FloatField()
    
    objects = models.GeoManager()
    
    def __unicode__(self):
        return u'%s (%s)' % (self.call_letters, self.frequency)
        
    def serialize(self):
        return {
            'frequency': "%.1f" % self.frequency,
            'call_letters': self.call_letters,
            'city': self.city,
            'state': self.state,
            'format': self.format,
            'location': {
                'lat': self.location.y,
                'lng': self.location.x
            }
        }