# This program is for adding two nos taken from user

name = input('What is your name? ')
print('Hello ' + name)

first_no = float(input('Provide first no. you want to add '))
#print('You provided first no. as ' + first_no)

second_no = float(input('Your second no. to add '))
#print('You provided the second no. as ' + second_no)

t = first_no + second_no

#output option 1
print('and total of those two nos is equal to: ', t)

#output option 2
print(t)

##output option 3
print('and total of those two nos is equal to: ' + str(t))
