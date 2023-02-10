print('Enter the 1st number')
num1 = input()
print('Enter the 2nd number')
num2 = input()

try:
    print('Sum of these number is',int(num1)+int(num2))
except Exception as a:
    print(a)

print("This line is very important")