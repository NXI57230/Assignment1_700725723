it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#• Find the length of the set it_companies

len(it_companies)

#• Add 'Twitter' to it_companies

it_companies.add('Twitter')
it_companies

#• Insert multiple IT companies at once to the set it_companies

it_companies.update(['Equifax','Cognizant'])
it_companies

#• Remove one of the companies from the set it_companies

it_companies.remove('Cognizant')
it_companies

#• What is the difference between remove and discard

it_companies.remove('Cognizant')
it_companies

it_companies.discard('Cognizant')
it_companies

#If we use remove for the same value after removing it throws an exception whereas for discard it does not throw any exception.

#• Join A and B

A.union(B)

#• Find A intersection B

A.intersection(B)

#• Is A subset of B

A.issubset(B)

#• Are A and B disjoint sets

A.isdisjoint(B)

#• Join A with B and B with A

A.union(B) and B.union(A)

#• What is the symmetric difference between A and B

A.symmetric_difference(B)

#• Delete the sets completely

del A
del B

#• Convert the ages to a set and compare the length of the list and the set.

set_ages = set(age)
set_ages
len(age),len(set_ages)
len(age) == len(set_ages)

