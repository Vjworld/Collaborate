#For Loop
# for item in list[1,2,3,]
# print(item)
#for item in range(10):
# print(item)
#for item in range(1,10):
#for item in range(1,10,2):
'''
prices = [10,20,30,40,50]
print(prices)
print(type(prices))
print('--------------')
#for item in prices:
tot = sum(prices [0:5])
print(f"Total = {tot}")
'''

#=============NESTED LOOPS====================
"""
print('''
XXXXX
XX
XXXXX
XX
XX
''')
"""
#--------------------------------
'''#Sol 1
letter = [5,2,5,2,2]

for item in letter:
    line1= 'X' * item
    print(line1)
#--------------------------------
#Sol 2
letter = [5,2,5,2,2]

for x in letter:
    output=''
    for count in range(x):
        output += 'x'
    print(output)
#--------------------------------'''

"""
print('''
X
X
X
X
XXXXXX''')
"""
#--------------------------------
alpha = [1,1,1,1,6]
for b in alpha:
    output=''
    for x in range(b):
        output += 'x'
    print(output)
