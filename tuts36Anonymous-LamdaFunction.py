# lambda functions or anonymous functions
# lambda - lambda function convenience ke liye hota hai

def add(a, b):
    return a + b

minus = lambda x, y: x - y

def minus(a, b):
    return a-b

print(minus(9,5))

def a_first(a):
    return a[1]

a = [[1, 14], [5, 6], [8, 23]]
# a.sort(key = lambda x:x[1])    #key - key argument hota jo function ko as a input leta hai
print(a_first(a))