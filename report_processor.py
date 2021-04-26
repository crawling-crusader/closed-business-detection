import json

with open("report_no_duplicate.txt") as f:
    content = f.readlines()

d = []
for line in content:
    c_dict = json.loads(line)
    d.append(c_dict["osm"]["distance"])

print(d)

