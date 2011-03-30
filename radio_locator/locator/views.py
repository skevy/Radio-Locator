import json

from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.gis.geos import Point

from radio_locator.locator.models import Station

def all_stations(request):
    if "lat" not in request.GET or "lng" not in request.GET:
        return HttpResponseNotFound()
        
    loc = Point(float(request.GET['lng']), float(request.GET['lat']))
    
    stations = {}
        
    stations['high'] = [s.serialize().update(distance=s.distance) for s in Station.objects.filter(local_range__contains=loc).distance(loc).order_by('-distance')]
    stations['medium'] = [s.serialize() for s in Station.objects.filter(distant_range__contains=loc).exclude(pk__in=[s['pk'] for s in stations['high']]).order_by('-frequency')]
    
    return HttpResponse(json.dumps(stations), mimetype="application/json")