import random

number = random.randint(1,51)
print(f'test: {number}')
global try_num
try_num = 0
rerun = 1
print("Guess the number!")
print("Type 'stop' to exit")
while rerun:
    try:
        quess = input("Put the number: ")
    except:
        print("Blee")
        continue
    try_num = try_num + 1
    if int(quess) == number:
        break
    elif int(quess) > number:
        print('Hidden number is lower')
    else:
        print('Hidden number is bigger')
print(f'Good work! You guess the number in {try_num} try')