import string
import matplotlib.pyplot as plt
import numpy as np
import csv

plt.style.use('_mpl-gallery')

# make data as empty lists
x = []
y = []
xmin = -1
xmax = -1
ymin = -1
ymax = -1

# read in file

# CSV reading tutorial https://www.geeksforgeeks.org/reading-csv-files-in-python/
with open('example_data.csv', mode='r')as file:
    csvFile = csv.DictReader(file)

    for lines in csvFile:
        xData = lines['Date'].replace("/", "")
        date = np.datetime64(
            '20' + xData[4:6] + '-' + xData[0:2] + '-' + xData[2:4])
        tempY = float(lines['Total AF'])
        x.append(date)
        y.append(tempY)
        if xmin == -1 or xmin > date:
            xmin = date
        if xmax == -1 or xmax < date:
            xmax = date
        if ymin == -1 or ymin > tempY:
            ymin = tempY
        if ymax == -1 or ymax < tempY:
            ymax = tempY

# read this for dates when you have time
# https://matplotlib.org/stable/api/dates_api.html?highlight=dates#matplotlib.dates.AutoDateLocator

xStep = (xmax-xmin)/10
yStep = (ymax-ymin)/20
# plot
fig, ax = plt.subplots()

ax.plot(x, y)  # [x values], [y values]

ax.set(xlabel='Date', ylabel='Total Acc AF',
       xticks=np.arange(xmin, xmax, xStep), yticks=np.arange(ymin, ymax, yStep))
plt.show()
