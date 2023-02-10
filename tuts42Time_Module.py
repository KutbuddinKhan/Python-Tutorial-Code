import time

initial = time.time()
k = 0
while k < 45:
    print("This is Kutbuddin Bhai")
    time.sleep(2)
    k += 1
print("While loop run in",time.time() - initial,"Second")

initial2 = time.time()
for i in range(45):
    print("This is Kutbuddin Bhai")
print("For loop run in",time.time() - initial2,"Second")

# localtime = time.asctime(time.localtime(time.time()))
#
# print(localtime)