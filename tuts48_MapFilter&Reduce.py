# map function kisi bhi ek function ko ek puri list me apply krdeta hai

# numbers = ["2", "4", "5"]
# print(numbers[2])

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

#########################Map#########################
# numbers = list(map(int,numbers))

# numbers[2] = numbers[2] + 1
# print(numbers[2])


# def square(a):
#     return a*a
#
# num = [2,3,4,5,6,2,4,5,8]
# sqr = list(map(square,num))
# print(sqr)

# map in lamda function
# num = [2,3,4,5,6,2,4,5,8,9]
# sqr = list(map(lambda x: x*x, num))
# print(sqr)

# def square(a):
#     return a * a
#
# def cube(a):
#     return a * a * a
#
# func = [square, cube]
# for i in range(5):
#     val = list(map(lambda x:x(i),func))
#     print(val)


###################Filter#######################
# filter function filter karta hai ye ek aisi list banata hai
# elements ki jis me ye given function True return krta hai.

# list_1 = [1,23,4,5,6,3,23,4,5,3,4,7,8,9]
# def is_greater_5(num):
#     return num>5
#
# gr_than_5 = list(filter(is_greater_5, list_1))
# print(gr_than_5)


#---------------------Reduce------------------
# reduce functools modules ka part hota hai

from functools import reduce

# list1 = [1,2,3,4]
# num = 0
# for i in list1:
#     num = num + i
# print(num)

list1 = [1,2,3,4]
num = reduce(lambda x,y:x+y, list1)
print(num)
