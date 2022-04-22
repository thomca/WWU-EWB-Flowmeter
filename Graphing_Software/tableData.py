import matplotlib.pyplot as plt
import numpy as np
import csv

plt.style.use('_mpl-gallery')

# make data as empty lists
x = []
y = []
xmin = 10110
xmax = 122630
ymin = 0
ymax = 80
xStep = (xmax-xmin)/20
yStep = (ymax-ymin)/20

# read in file

# CSV reading tutorial https://www.geeksforgeeks.org/reading-csv-files-in-python/
with open('example_data.csv', mode ='r')as file:
  csvFile = csv.DictReader(file)
 
  for lines in csvFile:
       tempX = lines['Date']
       x.append(int(tempX.replace("/", "")))
       y.append(float(lines['Total Acc AF']))
       

# plot
fig, ax = plt.subplots()

ax.plot(x, y) # [x values], [y values]

ax.set(xlabel='Date', ylabel='Total Acc AF', 
xticks=np.arange(xmin, xmax, xStep), yticks=np.arange(ymin, ymax, yStep))
plt.show()