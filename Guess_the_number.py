import random

choice_typ = ['y', 'n', 'Y', 'N']


def play_game():
    score = 0
    number = random.randint(1, 51)
    while True:
        guess = input("Put the number: ")
        if not guess.isdigit():
            if guess == 'n':
                print(f'Closing... Good Bye!')
                exit()
            print('Bad input! Please put number or \"n\" for exit')
        else:
            score += 1
            if int(guess) == number:
                print(f'Good work! You guess the number in {score} try')
                break
            elif int(guess) > number:
                print('Hidden number is lower')
            else:
                print('Hidden number is bigger')
    return


def main():
    print('Welcome into Geussing Game!')
    print('Your goal is to guess the number from range 1 to 50 in as few attempts as possible')
    while True:
        choice = (input('Should we start?\n \"y\" for start new game\n \"n\" for exit (works any time)\n')).lower()
        if choice in choice_typ:
            if choice == 'y':
                play_game()
            elif choice == 'n':
                print(f'Closing... Good Bye!')
                exit()
        else:
            print('Bad input!\nPlease type \"y\" for start or \"n\" for exit')


if __name__ == '__main__':
    main()
