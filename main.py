import random

print("WELCOME TO ROCK PAPER SCISSORS GAME")
print("The rule of the game :")
print("-> Rock beats Scissors")
print("-> Paper beats Rock")
print("-> Scissor beats Paper")



def Choose_Option():
    user_choice = input("Choose Rock, Paper or Scissors: ")
    if user_choice in ["Rock", "rock", "r", "R"]:
        user_choice = "r"
    elif user_choice in ["Paper", "paper", "p", "P"]:
        user_choice = "p"
    elif user_choice in ["Scissors", "scissors", "s", "S"]:
        user_choice = "s"
    else:
        print("I don't understand, try again.")
        Choose_Option()
    return user_choice

def Computer_Option():
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    else:
        comp_choice = "s"
    return comp_choice


while True:
    print("")
    
    user_choice = Choose_Option()
    comp_choice = Computer_Option()

    print("")
    
    if user_choice == "r":
        if comp_choice == "r":
            print("Player(Rock) : CPU(Rock) ")
            print("It's a tie.")
        
        elif comp_choice == "p":
            print(" Player(Rock) : CPU(Paper) ")
            print("You lose!")
            
        elif comp_choice == "s":
            print("Player(Rock) : CPU(Scissors)")
            print("You win!")

    elif user_choice == "p":
        if comp_choice == "r":
            print("Player(Paper) : CPU(Rock) ")
            print("You win!")
        
        elif comp_choice == "p":
            print("Player(Rock): CPU(Paper) ")
            print("It's a tie!")
            
            
        elif comp_choice == "s":
            print("Player(Paper) : CPU(Scissors) ")
            print("You lose!")

    elif user_choice == "s":
        if comp_choice == "r":
            print("Player(Scissors) : CPU(Rock)") 
            print("You lose!")
        
        elif comp_choice == "p":
            print("Player(Scissors) : CPU(Paper) ")
            print("You win!")
            
        elif comp_choice == "s":
            print("Player(Scissors) : CPU(Scissors)") 
            print("It's a tie!")

   
    
    user_choice = input("Do you want to play again? (y/n)")
    if user_choice in ["Y", "y", "yes", "Yes"]:
        pass
    elif user_choice in ["N", "n", "no", "No"]:
        print("Bye!")
        break
    else:
        break


