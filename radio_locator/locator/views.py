import json

from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.gis.geos import Point

from radio_locator.locator.models import Station

def all_stations(request):
    if "lat" not in request.GET or "lng" not in request.GET:
        return HttpResponseNotFound()
        
    loc = Point(float(request.GET['lng']), float(request.GET['lat']))
    
    stations = {}
    stations['high'] = []
    stations['medium'] = []
        
    high_stations = Station.objects.filter(local_range__contains=loc).distance(loc).order_by('distance')
    medium_stations = Station.objects.filter(distant_range__contains=loc).exclude(pk__in=[s['pk'] for s in stations['high']]).distance(loc).order_by('-frequency')
    
    for s in high_stations:
        station = s.serialize()
        station.update(distance=s.distance.m)
        print s.distance.m
        stations['high'].append(station)
    
    for s in medium_stations:
        station = s.serialize()
        station.update(distance=s.distance.m)
        print s.distance.m
        stations['medium'].append(station)
    
    return HttpResponse(json.dumps(stations), mimetype="application/json")