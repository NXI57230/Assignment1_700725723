#The following is a list of 10 students ages:
#ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

import numpy as np
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#• Sort the list and find the min and max age

ages.sort()
ages
m1 = min(ages)
m1
m2 = max(ages)
m2

#• Add the min age and the max age again to the list

ages.append(m1)
ages.append(m2)
ages

#• Find the median age (one middle item or two middle items divided by two)

ages.sort()
np.median(ages)

#• Find the average age (sum of all items divided by their number)

np.average(ages)

#• Find the range of the ages (max minus min)

r_ages = range(m1,m2)
r_ages
