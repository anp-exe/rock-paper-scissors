import random

computer = random.randint(1,3)
print(' 1 is for ✊Rock\n 2 is for ✋Paper.\n 3 is for ✌️Scissors.')
human = int(input("Pick a number: "))

print('Computer picked: ', computer)
print('You picked: ', human, '\n')

if computer == 1 and human == 1:
    print("It's a tie!")
elif computer == 2 and human == 1:
    print('You Lost!')
elif computer == 3 and human == 1:
    print('You Won!')
elif computer == 1 and human == 2:
    print('You Won!')
elif computer == 2 and human == 2:
    print('It\'s a tie!')
elif computer == 3 and human == 2:
    print('You Lost!')
elif computer == 1 and human == 3:
    print('You Lost!')
elif computer == 2 and human == 3:
    print('You Won!')
elif computer == 3 and human == 3:
    print("It's a tie!")
else:
    print('Please input a number between 1 and 3!')