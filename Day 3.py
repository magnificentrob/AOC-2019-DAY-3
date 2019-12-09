import matplotlib.pyplot as plt
import csv
import shapely 
from shapely.geometry import LineString, Point
import numpy as np

wireA = []
with open('wirea.txt') as csv_file:
    csvreader = csv.reader(csv_file, delimiter = ',')
    for item in csvreader:
        wireA += item
csv_file.close()
wireB = []
with open('wireb.txt') as csv_file:
    csvreader = csv.reader(csv_file, delimiter = ',')
    for item in csvreader:
        wireB += item
csv_file.close()

last_x = 0
last_y = 0
x_axis = []
y_axis = []
x_axis.append(0)
y_axis.append(0)

last_xB = 0
last_yB = 0
x_axisB = []
y_axisB = []
x_axisB.append(0)
y_axisB.append(0)

for wire in wireA:
    if wire[:1] == 'R':
       numberR = int(wire[1:])
       x_axis.append(last_x + numberR)
       y_axis.append(last_y)
       last_x = (last_x + numberR)
    if wire[:1] == 'L':
       numberL = int(wire[1:])
       x_axis.append(last_x - numberL)
       y_axis.append(last_y)
       last_x = (last_x - numberL)
    if wire[:1] == 'U':
       numberU = int(wire[1:])
       y_axis.append(last_y + numberU)
       x_axis.append(last_x)
       last_y = last_y + numberU
    if wire[:1] == 'D':
       numberD = int(wire[1:])
       y_axis.append(last_y - numberD )
       x_axis.append(last_x)
       last_y =  last_y - numberD

for wire in wireB:
    if wire[:1] == 'R':
       numberR = int(wire[1:])
       x_axisB.append(last_xB + numberR)
       y_axisB.append(last_yB)
       last_xB = (last_xB + numberR)
    if wire[:1] == 'L':
       numberL = int(wire[1:])
       x_axisB.append(last_xB - numberL)
       y_axisB.append(last_yB)
       last_xB = (last_xB - numberL)
    if wire[:1] == 'U':
       numberU = int(wire[1:])
       y_axisB.append(last_yB + numberU)
       x_axisB.append(last_xB)
       last_yB = last_yB + numberU
    if wire[:1] == 'D':
       numberD = int(wire[1:])
       y_axisB.append(last_yB - numberD )
       x_axisB.append(last_xB)
       last_yB =  last_yB - numberD

plt.plot(x_axis, y_axis, '-ro')
plt.plot(x_axisB, y_axisB, '--bo')
plt.show()

wire1 = zip(x_axis, y_axis)
wire2 = zip(x_axisB, y_axisB)
wire1 = list(wire1)
wire2 = list(wire2)

point_of_intersection = []
point_before_intersection = []
steps_to_intersection = []

for i in range(len(wire1)-1):
    pointA = wire1[i]
    pointB = wire1[i+1]
    for x in range(len(wire2)-1):
        pointC = wire2[x]
        pointD = wire2[x+1]
        line1 = LineString([pointA, pointB])
        line2 = LineString([pointC, pointD])
        int_pt = line1.intersection(line2)
        try:
            point_of_intersection.append((int_pt.x, int_pt.y))
            point_before_intersection.append((pointA, pointC))
            steps_to_intersection.append((i,x))
        except:
            pass

closest_intersection = []        
for item in point_of_intersection:
   closest_intersection.append(abs(item[0])+abs(item[1]))
closest_intersection.sort()
print(closest_intersection[1])
    
###final steps to intersection
num = np.subtract(point_before_intersection[1][0],point_before_intersection[1][1])
num = abs(num[0])+abs(num[1])
wireAsteps = steps_to_intersection[1][0]
wireBsteps = steps_to_intersection[1][1]

for i in wireA[:wireAsteps]:
    num += int(i[1:])
for i in wireB[:wireBsteps]:
    num += int(i[1:])    
print(num)