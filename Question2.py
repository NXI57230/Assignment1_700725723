#• Create an empty dictionary called dog
#• Add name, color, breed, legs, age to the dog dictionary

dog = { }
dog = {
'name' : 'Joe',
'color' : 'white',
'breed' : 'Bichon Frise',
'legs' : 'four',
'age' : '13 months'
}
dog

#• Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

student = {
'first_name' : 'Navasahitha',
'last_name' : 'Inuganti',
'gender' : 'Female',
'age' : 25,
'marital_status' : 'married',
'skills' : ['never give up attitude'],
'city' : 'St.Louis',
'address' : 'Basston Dr'
}
student

#• Get the length of the student dictionary

len(student)

#• Get the value of skills and check the data type, it should be a list

print(student['skills'])
print(type(student['skills']))

#• Modify the skills values by adding one or two skills

student['skills'].append('multi-tasking')
student

#• Get the dictionary keys as a list

student.keys()

#• Get the dictionary values as a list

student.values()
