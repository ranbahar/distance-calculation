import math

from point import Point


def haversine_distance(center_point: Point, checked_point: Point):
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [center_point.latitude, center_point.longitude, checked_point.latitude,
                                                checked_point.longitude])

    # Haversine formula
    distance_lat = lat2 - lat1
    distance_lon = lon2 - lon1
    a = math.sin(distance_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(distance_lon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Radius of earth in kilometers (mean value). You can change it to 3956 for miles.
    global_radius = 6371.01

    # Calculate the distance
    distance = global_radius * c

    return distance


def is_within_radius(first_point: Point, radius_km, second_point: Point):
    distance = haversine_distance(first_point, second_point)

    return distance <= radius_km
