# f = open("tuts26_1FileRead.txt","r")    #file pointer banate hai file pointer open ke zariye open hota hai
# open file pointer return krta hai
# open ka second argument mode hota hai

# f = open("tuts26_1FileRead.txt","rb")

# f = open("tuts26_1FileRead.txt","rt")   #r and t both are default mode
# content = f.read()
# print(content)

# for line in content:    #content print krne par character by character print hota hai
# for line in f:  #f ko print krne se line by line print hoga aor contenet = f.read() ko close krna padega
#     print(line,end="")

# content = f.read(400)  #f.read() is a function
# print("1 ",content)
#
# content = f.read(4)  #f.read() is a function
# print("2 ",content)

# f = open("tuts26_1FileRead.txt","rt")
# print(f.readline())   #readline() ek line print krta hai
# print(f.readline())
# print(f.readline())

f = open("tuts26_1FileRead.txt", "rt")
print(f.readlines())    #readlines() list me print krta hai

f.close()