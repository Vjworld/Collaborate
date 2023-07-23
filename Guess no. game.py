#Guess the number game

Lucky_no = 8

Guess_attempts = 0

Guess_limit = 3

while Guess_attempts < Guess_limit:
    Guess= int(input('Guess a number between "1 to 10" and type it in -> ')) 
    Guess_attempts += 1
    if Guess == Lucky_no:
        print("Wow, your guess is correct!")
        print("You Won!")
        break
else:
    print("Sorry you failed!")
        
