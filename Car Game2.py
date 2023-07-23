# This is the engine for a Car simulation game.
# It does not have/support a GUI
# it is to practice what we learnt so far [2Mar23].
#----------------------------------------------------
#4Mar23

command = ""
started = False

while True:
    command = input('> ').lower()
    if command == 'start':
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started.. Ready to go")
    elif command == 'stop':
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped.. Relax now")

    elif command == 'help':
        print("""
HELP Menu:
Start to start the car
Stop to stop the car
Quit to quit car game
Help to request help menu """)
    
    elif command == 'quit':
        print("No problem.. Relax and move out")
        break
    else:
        print("Sorry I don't understand that! please try again")




#=====================================================
#----------------------------------------------------
#4Mar23
'''
possible_user_inputs = ["Yes","no","Help"]

#Checking user input valid or not
#print(possible_user_inputs)
#print(type(possible_user_inputs))

user_name = input("Hey, What's your name? - ")
user_input1 = input(user_name + ', Type "Yes" to play "Car Game" otherwise "No" - ')

user_input = user_input1.upper()

while user_input not in possible_user_inputs:
    print("Sorry, I don't understand, please try again! ")
    break


    if user_input in possible_user_inputs == "NO":
        print("No Problem, Bye take care ! ")
        break
#---------------------------------------------------- 
if user_input == "YES":
    print("""
        Welcome to the Car Game !
           Here is the Menu:
           Type 'Start' to start the Car
           Type 'Stop' to stop the car
           Type 'Quit' to exit the Car Game
           Type 'Help' for Menu """)
    user_input2 = input(user_name + '> "Start" to start car engine!')
    print("Vroooom....Vroooom_Car started")
    user_input2 = input(user_name + '> "Stop" to stop car engine!')
    print('Wait for the car to stop, then type "Quit" ')
    user_input2 = input(user_name + '> "Quit" to quit Car Game!')

    if user_input2 == "Quit":
        print("Thanks for playing!")
        '''

    
#-------------------------
'''
else user_input == "YES":
        print("""
        Welcome to the Car Game !
           Here is the Menu:
           Type 'Start' to start the Car
           Type 'Stop' to stop the car
           Type 'Quit' to exit the Car Game
           Type 'Help' for Menu
           """)
        user_input2 = input('What do you want? - ')
        while user_input2.upper() != 'Quit':
            if user_input2.upper()!= 'Stop':
                elif user_input2.upper()!= 'Stop':
                print('Type "Start" to start car - ')
            print('Type "Start" to start car - ')
            
'''
'''
if user_input.upper() == "Yes":
    print("""
           Here is the Menu:
           Type 'Start' to start the Car
           Type 'Stop' to stop the car
           Type 'Quit' to exit the Car Game
           Type 'Help' for Menu
           """)
    user_input.upper() = input('your choice')
elif:
    user_input.upper() == 'Start'
    print("Starting the Car..vroom...vroom")
    print("Get ready to race....")
elif:
    user_input.upper() == 'Stop'
    print("Stopping the Car..screeech...screeech")
elif:
    user_input.upper() == 'Quit'
    print("Thank you for playing !")
elif:
    user_input.upper() == 'Help'
    print("""
           Here is the Menu:
           Type 'Start' to start the Car
           Type 'Stop' to stop the car
           Type 'Quit' to exit the Car Game
           Type 'Help' for Menu
           """)    
while user_input.upper() == "No"
        print("No Problem, Bye ! ")

        print("Sorry, I do not understand, Please try again ! ")
'''    

