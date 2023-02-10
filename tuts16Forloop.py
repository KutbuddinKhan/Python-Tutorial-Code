# list1 = [["Harry",2],["Larry",5],
#          ["Carry",6],["Marie",3]
#         ]
#
# dict1 = dict(list1)
#
# for item in dict1:
#     print(item)
# print(dict)

# print(list1[0],list1[1],list1[2],list1[3])

# for item, lollypop in dict.items():
#     print(item," and lolly is",lollypop)

###########Quiz###########
items = [int, float, "HaRry", 5, 3, 6, 3, 22, 21, 64, 23, 233, 23]

for item in items:
    if str(item).isnumeric() and item >= 6:
        print(item)