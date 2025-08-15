action = input("Enter your turn (rock, paper, or scissors): ")

if action == "rock":
    print("Computer turn: paper 'computer wins'")
elif action == "paper":
    print("Computer turn: scissors 'computer wins'")
elif action == "scissors":
    print("Computer turn: rock 'computer wins'")
else:
    print("Invalid input. Please choose rock, paper, or scissors.")