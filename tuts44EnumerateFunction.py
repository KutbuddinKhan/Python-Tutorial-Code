sabji = ["Bhindi", "Aloo", "Karela", "Parwar", "Lauki"]

# i = 1
# for item in sabji:
#     if i%2!=0:
#         print(f'Jarvis please buy{item}')
#     i += 1

# Enumerate function
for index, item in enumerate(sabji):
    if index % 2 == 0:
        print(f'Jarvis please buy {item}')