#The radius of a circle is 30 meters.
#• Calculate the area of a circle and assign the value to a variable name of _area_of_circle_

import math
radius = 10
_area_of_circle_ = math.pi*radius**2
_area_of_circle_

#• Calculate the circumference of a circle and assign the value to a variable name of _circum_of_circle_

_circum_of_circle_ = 2*math.pi*radius
_circum_of_circle_

#• Take radius as user input and calculate the area.

r = float(input("Enter the radius of circle = "))
area = math.pi*r**2
print('area of circle is : {0}'.format(area))
