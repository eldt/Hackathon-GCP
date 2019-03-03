from datetime import datetime

import googlemaps


def GeoScript(latvar, longvar):
    gmaps = googlemaps.Client(key= 'AIzaSyD98Jrf_CWeR-tEug615QX_rL6Y_qXjUsw')
    
    geo_code = gmaps.reverse_geocode((latvar, longvar))

    print(geo_code)
