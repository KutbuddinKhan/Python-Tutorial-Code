# f = open("tuts28_1WritingFile.txt","w")

# f = open("tuts28_1WritingFile.txt","a")
# f.write("Kutbuddin bhai bahut acche hai\n")

# f = open("tuts28_1WritingFile.txt","w")
# a = f.write("Kutbuddin bhai bahut acche hai\n")#number of character print krta hai
# print(a)
# f.close()

# f = open("tuts28_2WritingFile.txt","a")
# a = f.write("Kutbuddin bhai bahut acche hai\n")#number of character print krta hai
# print(a)
# f.close()

# # Handle read and write both
#
f = open("tuts28_2WritingFile.txt","r+")
print(f.read())

f.write("thank you!")