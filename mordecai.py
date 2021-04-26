from geopy.geocoders import geonames

geolocator = geonames.GeoNames();
geolocator.username = "leCaptain"
print(geolocator.geocode("Gateway of India"))