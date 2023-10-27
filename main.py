from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('map.html', google_maps_key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')


if __name__ == '__main__':
    app.run(debug=True)

# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# import gmaps
# import math
# import random
#
# # Constants
# R = 6371.0  # Radius of the Earth in kilometers
#
#
# def haversine(lat1, lon1, lat2, lon2):
#     """Calculate the great-circle distance between two points."""
#     dlat = math.radians(lat2 - lat1)
#     dlon = math.radians(lon2 - lon1)
#     a = (math.sin(dlat / 2) ** 2 +
#          math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
#          math.sin(dlon / 2) ** 2)
#     c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
#     distance = R * c
#     return distance
#
#
# def destination_point(lat, lon, bearing, distance):
#     """Find the destination point given starting point, bearing and distance."""
#     lat_rad = math.radians(lat)
#     lon_rad = math.radians(lon)
#
#     angular_distance = distance / R
#
#     lat2_rad = math.asin(math.sin(lat_rad) * math.cos(angular_distance) +
#                          math.cos(lat_rad) * math.sin(angular_distance) * math.cos(bearing))
#
#     lon2_rad = lon_rad + math.atan2(math.sin(bearing) * math.sin(angular_distance) * math.cos(lat_rad),
#                                     math.cos(angular_distance) - math.sin(lat_rad) * math.sin(lat2_rad))
#
#     lat2 = math.degrees(lat2_rad)
#     lon2 = math.degrees(lon2_rad)
#
#     return lat2, lon2
#
#
# def random_point_in_circle(center_lat, center_lon, radius):
#     """Get a random point within a circle defined by center and radius."""
#     random_distance = random.random() * radius
#     random_bearing = random.uniform(0, 2 * math.pi)
#
#     return destination_point(center_lat, center_lon, random_bearing, random_distance)
#
#
# # Example
# center_lat = 52.5200  # Berlin latitude
# center_lon = 13.4050  # Berlin longitude
# radius = 10  # in kilometers
#
# random_point = random_point_in_circle(center_lat, center_lon, radius)
# print(f"Random point in circle: Latitude: {random_point[0]}, Longitude: {random_point[1]}")
# # Initialize gmaps with your Google Cloud API key
# gmaps.configure(api_key="AIzaSyCxs_Hc9GVT5GYzaQdZB1nG7BIn07mwDac")
#
# center_lat = 52.5200  # Berlin latitude
# center_lon = 13.4050  # Berlin longitude
# radius = 10  # in kilometers
#
# # Getting a random point in the circle (using the function provided previously)
# random_point = random_point_in_circle(center_lat, center_lon, radius)
#
# # Create the map centered around the random point
# fig = gmaps.figure(center=random_point, zoom_level=13)
#
# # Add a marker for the random point
# marker = gmaps.marker_layer([random_point])
# fig.add_layer(marker)
#
# fig
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
