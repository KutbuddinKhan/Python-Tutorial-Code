with open("tuts28_1WritingFile.txt") as f:
    # a = f.read(9)
    a = f.readlines()
    print(a)

f = open("tuts28_1WritingFile.txt", "rt")
content = f.read()
print(content)
f.close()

# Question of the day:
# Yes or No
# Answer : Yes