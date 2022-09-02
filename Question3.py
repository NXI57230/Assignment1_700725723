#• Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

siblings = ('sahitha','yaswanth','santhi','bavina','priyansh')
siblings

#• Join brothers and sisters tuples and assign it to siblings

sisters = ('sahitha','santhi','bavina')
brothers = ('yaswanth','priyansh')
new_siblings = sisters + brothers
new_siblings

#• How many siblings do you have?

len(new_siblings)

#• Modify the siblings tuple and add the name of your father and mother and assign it to family_members

father = 'prasad'
mother = 'kiran'
family_members = new_siblings + (father,mother)
family_members
