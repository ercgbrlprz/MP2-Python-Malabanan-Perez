#Machine Problem 2
#Malabanan,Angelo-Perez,Eric
#2-ece-a

from math import *
x1 = int(input ('x1: '))
y1 = int(input ('y1: '))
x2 = int(input ('x2: '))
y2 = int(input ('y2: '))
x3 = int(input ('x3: '))
y3 = int(input ('y3: '))


D = (((x2**2)-(x1**2))*(y3-y1)+((y2**2)-(y1**2))*(y3-y1)+((x1**2)-(x3**2))*(y2-y1)+((y1**2)-(y3**2))*(y2-y1)) / ((y3-y1)*(x1-x2)-(x1-x3)*(y2-y1))
E = (((x1**2)-(x3**2))*(x1-x2)+((y1**2)-(y3**2))*(x1-x2)+((x2**2)-(x1**2))*(x1-x3)+((y2**2)-(y1**2))*(x1-x3)) / ((x1-x2)*(y3-y1)-(y2-y1)*(x1-x3))
F = - (x1**2) - (y1**2) - (D)*(x1) - (E)*(y1)

h = D / -2; k = E / -2
center = [h,k];

radius = sqrt((h **2) + (k**2) - (F))

solution = [D,E,F]

print('Center: ');print(center);
print('Radius: ');print(radius);
print('Solution for DEF: ');print(solution)

