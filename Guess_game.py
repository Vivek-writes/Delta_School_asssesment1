#Guess game


import random

def guess_game():
    
    expected_num = random.randint(1, 100)
    
    low = 1
    high = 100
    max_chance = 10
    chances = 0
    
    while chances < max_chance:
        chances += 1
        
        guess = (low + high) // 2
        
        print(f"Attempt {chances}:")
        user_guess = int(input("Guess the number between 1 to 100: "))

        if user_guess == expected_num:
            print("Congratulations! You guessed the number")
            break
        
        elif user_guess < expected_num:
            print("Too low! Try again")
            low = user_guess + 1
        
        else:
            print("Too high! Try again")
            high = user_guess - 1
guess_game()