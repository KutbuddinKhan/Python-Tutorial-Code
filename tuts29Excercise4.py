# Pattern printing
# Input = Integer n
# Boolean = True or False
#
# True n = 5
# *
# **
# ***
# ****
#
# False n = 5
# ****
# ***
# **
# *
#
# def pattern1():
#     for i in range(4):
#         for j in range(i + 1):
#             print("*",end=" ")
#         print()
#         return
#
#
# def pattern2():
#     for i in range(4):
#         for j in range(4 - i):
#             print("*",end=" ")
#         print()
#         return
# #
# print("how many row you want for print\n")
# row = int(input())
# print("Enter 0  and 1")
# user_input = int(input())
# boolean = int(input())
# if boolean==True:
#     print(pattern1())
# elif boolean == False:
#     print(pattern2())
# else:
#     print(pattern2())

# print("Enter the boolean value")
# user_input = bool(input())
#
# if user_input == 1:
#     for i  in range(4):
#         for j in range(i + 1):
#             print("*",end=" ")
#         print()
# elif user_input == 0:
#     for i in range(4):
#         for j in range(4 - i):
#             print("*",end=" ")
#         print()
# else:
#     print("Wrong Input")


print("How many row you want to print: ")
one = int(input())
print("Type 1 or 0")
two = int(input())
new = bool(two)

if new == True:
    for i  in range(1,one + 1):
        for j in range(1,i + 1):
            print("*",end=" ")
        print()
elif new == False:
    for i in range(one, 0, -1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
# else:
#     print("Wrong Input")

