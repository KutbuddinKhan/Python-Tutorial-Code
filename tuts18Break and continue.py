# i = 0
#
# while True:
#     if i + 1 < 5:
#         i = i + 1
#         continue    #current iteration jo chal rhi hai wahi chale bad wale sab bhool jaye
#
#     print(i + 1,end = " ")
#     if (i == 44):
#         break    #stop the loop
#
#     i = i + 1
# # loop break hone ke bad yaha ajayega

##############   Quiz   ##############
while True:
    inp = int(input("Enter the user input\n "))
    if inp > 100:
        print("Your input is greater than 100 \n")
        break
    else:
        print("Try agian\n")
        continue



