#Write a program, which reads weights (lbs.) of N students into a list and convert these weights to kilograms in a separate list using Loop. N: No of students (Read input from user)
#Ex: L1: [150, 155, 145, 148]
#Output: [68.03, 70.3, 65.77, 67.13]


weights = []
weight_in_kgs = []
no_of_students = int(input("Enter no of students: "))
print('Enter student weights in lbs:')
for i in range(0, no_of_students):
    weights.append(int(input()))

for i in range(0, no_of_students):
    weight_in_kgs.append(round(0.453592 * weights[i], 2))

print(weight_in_kgs)
