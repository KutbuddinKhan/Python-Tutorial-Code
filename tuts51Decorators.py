# def function1():
#     print("This is Decoration in Python")
#     print("This is Function1")
#
# func2 = function1
# # Quiz
# del function1   #Answer is Yes print hoga
# func2()

# ek function se ek function ko call kar skte hai
# def funcret(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return sum
# a = funcret(0)
# print(a)

# function ko ek argument ke taur pr bhi de skte hai
# def executor(func):
#     func("This is Function pass as a argument")
#
# executor(print)


# Decorated
def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("func1 Executed")
    return nowexec


@dec1
def who_is_kkhan():
    print("Kkhan is a good boy")


# who_is_kkhan = dec1(who_is_kkhan)     #ye line na likhte hue @dec1 bhi likh skte hai jaisa likha hua hai
who_is_kkhan()
