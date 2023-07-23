#Conditional Statements
#If, Else, Elif

# Print Downpayment for potential buyer based on his Good Credit score

'''
Good_credit = True

if Good_credit:
    print("Your Credit Score is above avg. ")
    print("You need to pay 10% as downpayment")

else:
    print("Your Credit Score is below avg. ")
    print("You need to pay 20% as downpayment")
'''
#---------------------------------------------

#Take name and credit score from user

name = input("Hi, What is your name ? ")
house_price = float(1000000) #1 Million
#print(house_price)

#Dynamic input from user
Good_credit = input(name + ", Do you have Good Credit Score (True or False)? ")

#Good_credit = True -> Manual input

if Good_credit:
    #print(Good_credit)
    print(name + ", Your Credit Score is above avg. ")
    print("You need to pay only 10% as downpayment!")
    print(f'Downpayment is {0.1 * house_price}')   
else:
    #print(Good_credit)
    print(name + ", Sorry but your Credit Score is below avg. ")
    print("You need to pay 20% as downpayment!")
    print(f'Downpayment is {0.2 * house_price}')


## Not working for true condition - need to revisit
