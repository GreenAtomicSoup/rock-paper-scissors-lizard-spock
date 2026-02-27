import random
import time

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def get_player_choice():
    options = ["rock", "paper", "scissors", "lizard", "spock"]
    print_slow("\nChoose your weapon! ✊📄✂️🦎🖖")
    print("  rock / paper / scissors / lizard / spock")
    while True:
        choice = input("> ").lower().strip()
        if choice in options:
            return choice
        elif choice.startswith(("r","p","s","l","sp")):  # shortcuts are fun
            for opt in options:
                if opt.startswith(choice):
                    return opt
        print_slow("Invalid choice... try again, human.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors", "lizard", "spock"])

def determine_winner(player, computer):
    # Using the famous Sheldon rules table as logic
    wins = {
        "rock":     ["scissors", "lizard"],
        "paper":    ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard":   ["paper", "spock"],
        "spock":    ["rock", "scissors"]
    }
    
    if player == computer:
        return "tie"
    elif computer in wins[player]:
        return "player"
    else:
        return "computer"

def main():
    print_slow("=====================================")
    print_slow("   ROCK PAPER SCISSORS LIZARD SPOCK   ")
    print_slow("      ...the Big Bang Theory edition! ")
    print_slow("=====================================\n")
    
    player_score = 0
    computer_score = 0
    rounds = 0
    
    while True:
        rounds += 1
        print(f"\nRound {rounds}  |  You: {player_score}  –  Computer: {computer_score}")
        
        player = get_player_choice()
        computer = get_computer_choice()
        
        print_slow(f"\nYou chose:     {player.upper()}")
        time.sleep(0.5)
        print_slow(f"Computer chose: {computer.upper()}")
        time.sleep(0.8)
        
        result = determine_winner(player, computer)
        
        if result == "player":
            player_score += 1
            print_slow(" → You WIN this round! 🎉")
        elif result == "computer":
            computer_score += 1
            print_slow(" → Computer wins... Skynet is coming 😈")
        else:
            print_slow(" → It's a TIE! ⚔️")
        
        again = input("\nPlay another round? (y/n): ").lower().strip()
        if again != 'y':
            break
    
    print_slow("\n================================")
    print_slow(f"     Final score after {rounds} rounds")
    print_slow(f"     You: {player_score}   –   Computer: {computer_score}")
    if player_score > computer_score:
        print_slow("     YOU ARE THE CHAMPION! 🏆")
    elif computer_score > player_score:
        print_slow("     Better luck next time... 🤖")
    else:
        print_slow("     It's a DRAW! Everyone is awesome")
    print_slow("================================\n")

if __name__ == "__main__":
    main()
