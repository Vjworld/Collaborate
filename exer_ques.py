
    
"""
name = input("What is your Name ? ")
print(" Hi " + name) 

color = input('Which is your favorite color? ')
print(name + ", Your favorite color is- " + color)
"""

#Take DOB and Calculate age

name = input("Hi, What is your Name ? - ")
#print("Please provide your DOB in DD/MM/YYYY format ")

dob = input( name + ", What is your DOB(DD/MM/YYYY)? - ")
print(dob)

print(name + ", You provided DOB as = " + dob)

dob1 = str(dob)
print(dob1[-4:])
#print(type(dob))

birth_year = int(dob1[-4:])
print(birth_year)
print(type(birth_year))

age = str(2023 - birth_year)
print(name + ", Your age is = " + age)

#How to extract the birth year from DD/MM/YYYY input??

"""
# Today's DATE
>>> from datetime import datetime
>>> datetime.today().strftime('%Y-%m-%d')
'2021-01-26'


>>> datetime.today().strftime('%Y-%m-%d %H:%M:%S')
'2021-01-26 16:50:03'


"""
