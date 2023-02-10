# n = 18
# number of guesses 9
# print no of guesses left
# no of guesses he took to finish
# game over

winning_number = 20

print("This is a number gussing game")
input_number = int(input("Guess Your Number between 1 to 100: "))

guess = 1
game_over = False

while not game_over:
    if winning_number == input_number:
        print("You win! and you guess the number in (guess)time ")
        game_over = True
    else:
        if winning_number >input_number:
            print("You Guess too low! ")
            guess = guess + 1
            input_number = int(input("Guess again:"))
        else:
            print("You guess too high! ")
            guess = guess + 1
            input_number = int(input("Guess again:"))