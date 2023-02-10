# Excercise 2 - faulty Calculator
# 45 * 3 = 555, 56 + 9 = 77, 56 / 6 = 4
# Design a calculator which will correctly solve all the problem except
# the following ones:
# 45 * 3 = 555, 56 + 9 = 77, 56 / 6 = 4
# your program shoulf take operator and the two numbers as input from the user
# and then return the result.
num1 = int(input("enter 1st number"))
num2 = int(input("enter 2nd number"))
# choice = int(input('what you want:'\n '+' for Addition \n '-' for Subtraction \n '*' for Multiplication\n '/' for Division \n '%'for Modulus))
print('so what you want?\n'+' + for Addition\n - for subtraction\n / for Division \n % for Modulus \n * for Multiplication')
choice = input()
if num1 == 45 and num2 == 3 and choice == '*':
    print("555")
elif num1 == 56 and num2 == 9 and choice == "+":
    print("77")
elif num1 == 56 and num2 == 6 and choice == "/":
    print("4")
elif choice == '+':
    plus = num1 + num2
    print(plus)
elif choice == '-':
    subtractoin = num1 - num2
    print(subtractoin)
elif choice == '*':
    multiplication = num1 * num2
    print(multiplication)
elif choice == '/':
    division = num1 / num2
    print(division)
elif choice == '%':
    modulus = num1 % num2
    print(modulus)
else:
    print('Wrong choice')


