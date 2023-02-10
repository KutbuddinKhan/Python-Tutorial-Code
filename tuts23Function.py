# function code ko reusebility ke liye use krte hai
# a = 8
# b = 9
# c = sum((a,b)) #built in function

# def function1(a , b):  #user define function
#     print("Hello you are in function 1",a + b)
#
# function1(5, 7)
# function1()
# function1()
# print(function1())

def function2(a, b):    #def is a keyword
    """This is a function which will calculate average of two numbers"""    # it is a doc Strings
    average = (a + b)/2
    # print(average)
    return average  #return function option hota hai

# v = function2( 5 , 7)
# print(v)
print(function2.__doc__)

