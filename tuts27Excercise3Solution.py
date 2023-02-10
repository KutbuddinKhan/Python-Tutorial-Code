# n = 18
# number of guesses 9
# print no of guesses left
# no of guesses he took to finish
# game over

# Solution
n = 18
number_of_guesses = 1
print("Numbers of guesses is limited to only 9 times: ")
while number_of_guesses <= 9:
    guess_number = int(input("Guess the number : \n"))
    if guess_number < 10:
        print("You enter less number please enter greater number\n")

    elif guess_number > 18:
        print("You enter greater number please input smaller number.\n ")

    else:
        print("You won\n")
        print(number_of_guesses," no.of guesses he took to finish. ")
        break
    print(9-number_of_guesses, " no.of guesses left")
    number_of_guesses = number_of_guesses + 1

if number_of_guesses > 9:
    print("game over.")