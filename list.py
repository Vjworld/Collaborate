#List
#program to find largest number in the list

numbers = [23,54,76,12,6,34,98,1,43,77]
#print(len(numbers))
#print(type(len(numbers)))

#print(numbers[0] // numbers[1])

#simplest solution
#a = sorted(numbers)
#print(f'Largest number is {a[-1]}')

''' Trial
for z in range(len(numbers)):
    Largest_num = ""
        if (numbers[0] // numbers[1]) == 0:
        Largest_num = numbers[1]
        print(Largest_num)
        break

    else:
        Largest_num = numbers[0]
        print(Largest_num)
        break
         
'''
#----------------Solution
max_n = numbers[0]

for number in numbers:
    if number > max_n:
        max_n = number
print(max_n)
print(f'Largest number is "{max_n}"')
