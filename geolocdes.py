from datetime import datetime
from datetime import timedelta
from geolocation.main import GoogleMaps
from geolocation.distance_matrix.client import DistanceMatrixApiClient
import time
import responses
import googlemaps


def geoloc(latvar, longvar, nlat, nlong):

    gmap = googlemaps.Client(key= 'AIzaSyD98Jrf_CWeR-tEug615QX_rL6Y_qXjUsw')

    reverse_geocode_starting = gmaps.reverse_geocode((latvar, longvar))

    reverse_geocode_destination = gmaps.reverse_geocode((nlat, nlong))

    directions_result = gmaps.directions("reverse_gecode_starting", "reverse_geocode_destination", mode="transit", departure_time=now)
