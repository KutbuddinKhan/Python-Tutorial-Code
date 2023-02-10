# F string
import math

# me = "Kkhan"
# a = "this is %s"%me
# print(a)

me = "Kkhan"
a1 = 3
# a = "this is %s %s"%(me, a1)
a = "This is {1} {0}"
b = a.format(me, a1)
print(b)

# f string
a = f"This is {me} {a1} {math.cos(90)}"
print(a)