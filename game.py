import random
import os
import time

# ASCII art for each choice
art = {
    "stone": """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """,
    "paper": """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """,
    "scissor": """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """
}

choices_list = ["stone", "paper", "scissor"]

# Function to clear screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Function to get user's choice (numbers)
def get_user_choice():
    print("Choose your move:")
    print("1️⃣ Stone")
    print("2️⃣ Paper")
    print("3️⃣ Scissor")
    
    choice = input("Enter your choice (1-3): ").strip()
    
    while choice not in ["1", "2", "3"]:
        print("Invalid choice. Please enter 1, 2, or 3.")
        choice = input("Enter your choice (1-3): ").strip()
    
    return choices_list[int(choice) - 1]

# Function to get computer's choice
def get_computer_choice():
    return random.choice(choices_list)

# Function to determine winner
def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "stone" and computer == "scissor") or \
         (user == "paper" and computer == "stone") or \
         (user == "scissor" and computer == "paper"):
        return "user"
    else:
        return "computer"

# Main game loop
def play_game():
    user_score = 0
    computer_score = 0

    while True:
        clear()
        print("=== 🪨📄✂️ Stone Paper Scissors ===")
        print(f"Score: You {user_score} | Computer {computer_score}\n")

        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print("\nYou chose:")
        print(art[user_choice])
        print("Computer chose:")
        print(art[computer_choice])

        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print("🤝 It's a tie!")
        elif result == "user":
            print("🎉 You win this round!")
            user_score += 1
        else:
            print("💻 Computer wins this round!")
            computer_score += 1

        time.sleep(1.5)

        # Ask if player wants to play again
        again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if again != "y":
            print("\nFinal Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            if user_score > computer_score:
                print("🏆 Congratulations, you beat the computer!")
            elif user_score < computer_score:
                print("😢 The computer won this time. Better luck next time!")
            else:
                print("🤝 It's an overall tie!")
            break

if __name__ == "__main__":
    play_game()