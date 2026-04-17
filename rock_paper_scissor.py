import random

choices = ['rock', 'paper', 'scissor']

# What beats what
win_map = {
    'rock': 'scissor',
    'paper': 'rock',
    'scissor': 'paper'
}

def get_computer_move():
    return random.choice(choices)

def find_winner(user, comp):
    if user == comp:
        return "Tie"
    elif win_map[user] == comp:
        return "User Won"
    else:
        return "Computer Won"

print("===== Rock Paper Scissor =====")

while True:
    if input("Play? (y/n): ").lower() != 'y':
        print("Bye")
        break

    move = input("r/p/s: ").lower()

    if move not in ['r', 'p', 's']:
        print("Invalid input\n")
        continue

    user_move = {'r': 'rock', 'p': 'paper', 's': 'scissor'}[move]
    computer_move = get_computer_move()

    print("User:", user_move)
    print("Computer:", computer_move)
    print(find_winner(user_move, computer_move), "\n")
