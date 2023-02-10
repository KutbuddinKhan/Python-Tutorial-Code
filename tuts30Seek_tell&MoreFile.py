f = open("tuts28_1WritingFile.txt")
# print(f.tell())   #tell() bata ta hai ke file pointer ki current location kya hai
print(f.readline(),end="")
# print(f.tell())

f.seek(0)  #seek() file pointer ko reset krke le ata hai us point pr jo input diye rhte hai

print(f.readline(),end="")
# print(f.tell())

# f.seek(20)  #seek() file pointer ko reset krke le ata hai us point pr jo input diye rhte hai

print(f.readline(),end="")
# print(f.tell())

f.close()
