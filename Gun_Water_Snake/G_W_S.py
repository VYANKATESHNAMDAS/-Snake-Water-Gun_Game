import random
import os
from setup.sprint import sprint
from setup.colors import c, r, ran, lr, lc, lg, g, ly, y
from setup.banner import banner, banner2, clear

# Function to determine the winner
def gamewin(comp, you):
    if comp == you:
        return None
    elif (comp == 's' and you == 'w') or (comp == 'w' and you == 'g') or (comp == 'g' and you == 's'):
        return False
    else:
        return True

# Main game loop
def play_game():
    os.system("clear")
    banner()
    n = 5  # Number of rounds
    for i in range(n):
        print("Comp turn: Snake (s), Water (w), Gun (g)?")
        
        # Randomly choose for the computer
        comp = random.choice(['s', 'w', 'g'])
        
        # User's turn
        you = input("Your turn: Snake (s), Water (w), Gun (g)? ").lower()
        while you not in ['s', 'w', 'g']:
            you = input("Invalid input. Please choose Snake (s), Water (w), or Gun (g): ").lower()
        
        # Determine the winner
        result = gamewin(comp, you)
        
        # Print results
        print(f"Computer chose: {comp}")
        if result is None:
            print("The game is a tie!")
        elif result:
            print("YOU WIN!")
        else:
            print("YOU LOSE!")
        
        # Ask if the user wants to play again
        if i < n - 1:
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again != 'y':
                break

if __name__ == "__main__":
    play_game()
