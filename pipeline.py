import time
import statistics
from input_processing import *
from geocode_utils import *
from distance_utils import *


def geocode_source_result(input_file, output_file):
    osm_not_found = 0
    routing_not_found = 0
    with open(input_file, encoding="utf-8") as f:
        content = f.readlines()

    with open(output_file, "w") as f:
        for line in content:
            try:

                report_dict = {
                    "title": "some report yo",
                    "source": {
                        "coord": {
                            "lat": "0.0",
                            "lon": "0.0"
                        },
                        "name": "",
                        "address": "",
                        "search_string": ""
                    },
                    "osm": {
                        "lat": "0.0",
                        "lon": "0.0",
                        "distance": "0",
                        "address": ""

                    }

                }
                content_dict = json.loads(line)
                # print(content_dict)
                distance_between = 0
                routing_coordinate_not_found = get_routing_coordinates(content_dict)
                if routing_coordinate_not_found is not "NotFound":
                    report_dict["source"]["coord"]["lat"] = routing_coordinate_not_found[0]
                    report_dict["source"]["coord"]["lon"] = routing_coordinate_not_found[1]
                    name = get_name(content_dict)
                    address = get_address(content_dict)
                    report_dict["source"]["address"] = address
                    if name is not "NotFound":
                        report_dict["source"]["name"] = name
                        search_string = remove_duplicates(name + " " + address)
                        report_dict["source"]["search_string"] = search_string
                    osm_lat_lon = forward_geocode(search_string)
                    if osm_lat_lon is not "NotFound":
                        report_dict["osm"]["lat"] = osm_lat_lon[0]
                        report_dict["osm"]["lon"] = osm_lat_lon[1]
                        time.sleep(2)
                        distance_between = distance_between_coordinates(osm_lat_lon, routing_coordinate_not_found)
                        # print(distance_between)
                        trim = str(distance_between).split()[0]
                        report_dict["osm"]["distance"] = trim
                        # print(content_dict)
                        # print(report_dict)
                    else:
                        osm_not_found += 1
                else:
                    routing_coordinate_not_found += 1

                osm_address = reverse_geocode(str(routing_coordinate_not_found[0]), str(routing_coordinate_not_found[1]))
                if osm_address is not "NotFound":
                    report_dict["osm"]["address"] = str(osm_address)

                f.write(json.dumps(report_dict))
                f.write("\n")
            except Exception as e:
                print(e)
    f.close()
    print("OSM NOT FOUND \t" + str(osm_not_found))
    # print("DISPLAY NOT FOUND \t" + str(routing_coordinate_not_found))

#
# def analyse_report(output_file):
#     print(output_file)
#     with open(output_file) as f:
#         output_content = f.readlines()
#
#     for oc in output_content:
#         oc_dict = json.loads(oc)
#         dd = oc_dict["osm"]["distance"]
#         print(type(dd))
#         dd_lsit = []
#         if dd is not "0":
#             dd_lsit.append(dd)
#
#     print(statistics.mean(dd_lsit))
#     print(statistics.median(dd_lsit))
#     print(statistics.stdev(dd_lsit))


if __name__== '__main__':
    input_file = "input/india_sample_demo.txt"
    output_file = "output/india_sample_demo_result_final.txt"

    # input_file = "input/sample30.txt"
    # output_file = "output/sample30_demo_result_final.txt"
    geocode_source_result(input_file, output_file)





