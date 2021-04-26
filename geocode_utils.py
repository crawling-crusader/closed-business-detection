from geopy.geocoders import Nominatim
from geopy.geocoders import GeoNames
import collections

nom = Nominatim()
geo_name = GeoNames(username="lecaptain", user_agent="sanity_check")

Point = collections.namedtuple('Point', ['x', 'y'])


# return named tuple
def forward_geocode(address):
    geo = collections.namedtuple('lat', 'lon')
    rev_value = nom.geocode(address)
    if  rev_value is not None:
        geo = Point(rev_value.latitude, rev_value.longitude)
        return geo
    return "NotFound"


def reverse_geocode(lat, lon):
    req_string = lat + ',' + lon
    print(req_string)
    res = nom.reverse(req_string)
    if res is not None:
        return res
    return "NotFound"



def reverse_geocode2(lat, lon):
    r = lat+','+lon
    res = nom.reverse(r)
    # print(type(res))

# if __name__ == '__main__':
#     lat = '28.65596'
#     lon = '77.23694'
#     k = (lat, lon)
#     h = reverse_geocode(lat, lon)
#     print(h)
#     add = "East of Kailash South East Delhi"
