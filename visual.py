import matplotlib.pyplot as pl

with open("distance_report.txt") as f:
    content = f.readlines()

d_list = []
label = ['distance']
for line in content:
    d_list.append(line)

pl.bar(d_list, label)
pl.show()