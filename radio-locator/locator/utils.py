from django.contrib.gis.geos import Point, Polygon

"""
Creates a circular polygon of given radius "rad" centered around a point "center"
"""
def circle_polygon(rad, center):
    d2r = math.pi / 180
    circle_points = []
    circle_lat = (rad / 3963.189) / d2r #in miles
    circle_lng = circle_lat / math.cos(center.y * d2r)
    
    for i in range(0, 361):
        theta = i * d2r
        lat = center.y + (circle_lat * math.sin(theta))
        lng = center.x + (circle_lng * math.cos(theta))
        point = Point(lng, lat)
        circle_points.append(point)