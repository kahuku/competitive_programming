def compare(u1, u2):
    if u1 == u2:
        return "It's a tie!"
    elif u1 == "rock":
        if u2 == "scissors":
            return "Player 1 wins!"
        elif u2 == "paper":
            return "Player 2 wins!"
    elif u1 == "scissors":
        if u2 == "rock":
            return "Player 2 wins!"
        elif u2 == "paper":
            return "Player 1 wins!"
    elif u1 == "paper":
        if u2 == "rock":
            return "Player 1 wins!"
        elif u2 == "scissors":
            return "Player 2 wins!"

while True:

    mov1 = input("Player 1: Select rock, paper, or scissors: ")
    mov2 = input("Player 2: Select rock, paper, or scissors: ")
    print(compare(mov1, mov2))

    again = input("Enter Y to play again... \n")
    if again != "Y":
        break
