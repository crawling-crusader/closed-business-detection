'''
geopy calculates geodesic distance or great-circle distance
multiple ellipsoidal model : most accurate depends on where you are located
'''

from geopy import distance

# source = (17.6583195, 75.9248021)
# dest =(17.66949615 ,75.9142412435102)


def distance_between_coordinates(src_lat, src_lon, resp_lat, resp_lon):
    source = (src_lat, src_lon)
    dest = (resp_lat, resp_lon)
    return distance.distance(source, dest)


def distance_between_coordinates(src_coord, dest_coord):
    return distance.distance(src_coord, dest_coord)


def distance_between_coordinates_great_circle(src_lat, src_lon, resp_lat, resp_lon):
    source = (src_lat, src_lon)
    dest = (resp_lat, resp_lon)
    return distance.great_circle(source, dest)


def distance_between_coordinates_great_circle(src_coord, dest_coord):
    return distance.great_circle(src_coord, dest_coord)


# s = (18.4974, 73.8477)
# d = (26.9169739, 75.7962)
# di = distance_between_coordinates_great_circle(s,d)
# print(di)
# # print(distance_between_coordinates(s, d))
# print(str(di).split()[0])