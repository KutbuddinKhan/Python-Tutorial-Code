print(f'For Snake type : 0\nfor Water type: 1\nFor Gun type: 2')
n = 1
com_point = 0
human_point = 0

while n <= 10:
    import random
    game = ['snake', 'water', 'gun']

    human = int(input("Enter your item:\n"))

    def func1():
        pc = random.choice(game)
        return pc
print(func1())

if func1() == game[human]:
    print('Draw')

elif (func1() == game[0] and human == 2) or (func1() == game[2] and human == 1) or (func1() == game[1] and human== 0):
    print('You Win!')
    human_point = human_point + 1

else:
    print('You lose')
    com_point = com_point + 1
print(f'{10 - n} matches left ')

n = n + 1
print(f'You win {human_point} times')
print(f'You lose {com_point} times')
print(f'Match draw {n - 1 - (human_point + com_point)} times')
print('\n')

if human_point < com_point:
    print('You lose the game'.upper())
elif com_point < human_point:
    print('You won the game'.upper())
else:
    print("Match draw")