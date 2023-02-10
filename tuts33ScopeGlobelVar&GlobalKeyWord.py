# l = 10 #Global Variable
#
# def function1(n):
#     # l = 5   #Local Variable
#     m = 10  #Local Variable
#     global l    #This is gloabal key word use for change value of global variable
#     l = l + 40
#     print(l, m)
#     print(n , "i hava printed")
#
# function1("This is me")
# # print(l)

x = 89
def kkhan():
    x = 20
    def kasim():
        global x
        x = 30
    print('Before calling kasim()',x)
    kasim()
    print('After calling kasim()',x)

kkhan()
print(x)


