from distance_utils import *
from input_processing import *



with open("output/sample30_result.txt", encoding='utf-8') as f:
    content = f.readlines()

for line in content:
    c_dict = json.loads(line)
    print(c_dict["osm"]["distance"])
    if c_dict["osm"]["distance"] == "0.0":
        print(c_dict["source"]["name"])