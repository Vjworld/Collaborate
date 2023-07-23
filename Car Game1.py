# This is the engine for a Car simulation game.
# It does not have/support a GUI
# it is to practice what we learnt so far

'''
#--------input always returns a 'str'
Play_game = input('Do you want to play a "Car Game" -> Enter Yes or No ? _ ')
print(Play_game) - to check user input
print(type(Play_game)) - to check data type of input
#--------

#--------Bool turns anything into True only - so cannot use here. 
Play_game = bool(Play_game)
print(Play_game)
print(type(Play_game))
#--------
'''

# condition is user input can be either of -> Yes, No, Other

user_input = input('Do you want to play a "Car Game" -> Enter Yes or No ? >')
#print(user_input)

if user_input == 'No':
        print("No problem, Thank you! Have a wonderful day!")
        
while user_input == 'Yes':
        print("Let's Start the Car Game")
        print('''Here is the "Help Menu"
          Type "Help" for the "Help" Menu
          Type "Start" for starting the Car
          Type "Stop" for stopping the Car
          Type "Quit" to exit the "Car Game"
          ''')
        user_input = input('Type "Start" for starting the Car >')

        if user_input == 'Start':
            print('''         Vroom...Vroom
                The Car Started...Get Ready to Race...''')
        #break - to check if it works
    
        user_input = input('Type "Stop" for stopping the Car - ')
        if user_input == 'Stop':
            print('''         sss....rrrr....
                The Car Stopped...Take rest...''')
        #break
    
        user_input = input('Type "Quit" to exit the "Car Game" - ')
        if user_input == 'Quit':
            print('''     Exiting the "Car Game"....
                      The Car Stopped...''')
        #break
else:
        print("Sorry I did not understand!")
        print("Please try again...")



