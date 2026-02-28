import polyline
import math
def decode_route_polyline(route):
    return polyline.decode(route["polyline"])
def haversine(coord1, coord2):
    radius = 6371  
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = (math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2)
    return 2 * radius * math.atan2(math.sqrt(a), math.sqrt(1 - a))
def compute_total_distance(points):
    distance = 0
    for i in range(len(points) - 1):
        distance += haversine(points[i], points[i + 1])
    return distance