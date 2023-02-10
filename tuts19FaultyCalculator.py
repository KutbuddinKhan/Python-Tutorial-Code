# Ek faulty Calculator excersie 15 me hai but wo withour function hai
###############  Faulty Calculator using Function  ###############
def calculator():
    print("\n Welcome to Calculator: This is Developed by Kutbuddin Khan")
    operation = input(''' please type in the math operation you would like to complete:
                      + for Additioin
                      - for Subtraction
                      * for Multiplication
                      / for Division
                      ** for Power
                      % for modulo
                      
                      Enter your Choice:
                      ''')
    num1 = int(input("Enter first Number: "))
    num2 = int(input("enter second Number:"))

    if operation == '+':
        if num1 == 56 and num2 == 9 and operation == '+':
            print("56 + 9 = 77")
        else:
            print(f"{num1}+{num2} = {num1 + num2}")

    elif operation == '-':
        print(f"{num1}-{num2} = {num1 - num2}")

    elif operation == '*':
        if num1 == 45 and num2 == 3 and operation == '*':
            print("45 * 3 = 555")
        else:
            print(f"{num1} * {num2} = {num1 * num2}")

    elif operation == '/':
        if num1 == 56 and num2 == 6 and operation == '/':
            print("56 / 6 = 4")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")

    elif operation == '**':
        print(f"{num1} ** {num2} = {num1 ** num2}")

    elif operation == '%':
        print(f"{num1} % {num2} = {num1 % num2}")
    else:
        print("You Press a Invalid Key")
    again()


def again():
    cal_again = input('''
    Do you want to calculate again?
    Please type y for YES or n for NO.
    ''')

    if cal_again == 'y':
        calculator()
    elif cal_again == 'n':
        print("See You Later")
    else:
        again()


calculator()

# def calculetor():
#     print("\nWellcome to Calculator: This is developed by Kutbuddin Khan")
#     operation = input('''
#     Please type in the math operation you would like to complete:
#     + for addition
#     - for subtraction
#     * for multiplication
#     / for division
#     ** for power
#     % for modulo
#
#     Enter Your Choise:
#     ''')
#
#     num1 = int(input("Enter first Number: "))
#     num2 = int(input("Enter second Number: "))
#
#     if operation == '+':
#         if num1 == 56:
#             print("56 + 9 = 77")
#         else:
#             print(f"{num1} + {num2} = {num1 + num2}")
#     elif operation == '-':
#         print(f"{num1} - {num2} = {num1 - num2}")
#     elif operation == '*':
#         if num1 == 45:
#             print("45 * 3 = 555")
#         else:
#             print(f"{num1} * {num2} = {num1 * num2}")
#     elif operation == '/':
#         if num1 == 56:
#             print("56/6 = 4")
#         else:
#             print(f"{num1} / {num2} = {num1 / num2}")
#     elif operation == '**':
#         print(f"{num1} ** {num2} = {num1 ** num2}")
#     elif operation == '%':
#         print(f"{num1} % {num2} = {num1 % num2}")
#     else:
#         print("You Press a Invalid Key")
#     again()
#
#
# def again():
#     cal_again = input('''
#     Do you want to calculate again?
#     Please type y for YES or n for NO.
#     ''')
#
#     if cal_again == 'y':
#         calculetor()
#     elif cal_again == 'n':
#         print("See You Later")
#     else:
#         again()
#
#
# calculetor()
