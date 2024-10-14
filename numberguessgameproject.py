import random
logo = '''     \/    wWw  wWw   wWw   oo_    oo_       (o)__(o)\\  //  wWw      \\\  ///wWw  wWw\\\    /// ___    wWw ()_()  
    (OO)   (O)  (O)   (O)_ /  _)-</  _)-<    (__  __)(o)(o)  (O)_     ((O)(O))(O)  (O)((O)  (O))(___)__ (O)_(O o)  
  ,'.--.)  / )  ( \   / __)\__ `. \__ `.       (  )  ||  ||  / __)     | \ || / )  ( \ | \  / | (O)(O)  / __)|^_\  
 / /|_|_\ / /    \ \ / (      `. |   `. |       )(   |(__)| / (        ||\\||/ /    \ \||\\//|| /  _\  / (   |(_)) 
 | \_.--. | \____/ |(  _)     _| |   _| |      (  )  /.--.\(  _)       || \ || \____/ ||| \/ || | |_))(  _)  |  /  
 '.   \) \'. `--' .` \ \_  ,-'   |,-'   |       )/  -'    `-\ \_       ||  ||'. `--' .`||    || | |_)) \ \_  )|\\  
   `-.(_.'  `-..-'    \__)(_..--'(_..--'       (             \__)     (_/  \_) `-..-' (_/    \_)(.'-'   \__)(/  \) '''
def game_function(user_lives):
    while user_lives != 0:
        print(f"You have {user_lives} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if user_guess > computer_guess:
            print("Too high.")
            print("Guess Again")
            user_lives -= 1
        elif user_guess < computer_guess:
            print("Too low.")
            print("Guess Again")
            user_lives -= 1
        else:
            print(f"You got it! The answer was {computer_guess}")
            break
    if user_lives == 0:
        print(f"You've run out of guesses, you lose. The number was {computer_guess}")

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
computer_guess = random.randint(1, 100)
choose_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if choose_level == "easy":
    lives = 10
    game_function(lives)
elif choose_level == "hard":
    lives = 5
    game_function(lives)
else:
    print("Wrong Input, DUMBO!")