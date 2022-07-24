

# Create a number guessing game.
import random




def makeguess():
    try:
        print()
        guess = int(input("Enter your guess: "))
        if(guess < 1 or guess > 10):
            print("Please enter a number between 1 and 10")
            makeguess()
        else:
            return guess
    except(ValueError or TypeError):
        print("Unsupported Character.\nPlease enter a valid number between 1 and 10")
        return makeguess()


def number_guessing():
    random_number = random.randint(1, 10)
    for i in range(5):
        while True:
            try:
                x = int(input('Enter your guess: '))
                if 0 <= x <=10:
                    break
                else:
                    print('Please enter a number between 1 and 10')
            except Exception as err:
                print(err)

        d = abs(random_number - x)
        if d == 0:
            print('Its a match! Congrats')
            return
        elif d in [9, 8]:
            stat = 'very cold'
        elif d in [7, 6]:
            stat = 'cold'
        elif d in [5, 4]:
            stat = 'neutral'
        elif d == 3:
            stat = 'warm'
        elif d < 2:
            stat = 'hot'

        if x < random_number:
            print(f'Your guess is cold from left and {stat} from right. Try again')
        else:
            print(f'Your guess is {stat} from left and cold from right. Try again')


while(True):
    print('1. Play again'   '1. Start the Game')
    print('2. Exit')
    choice = int(input('Enter your choice: '))
    if choice == 1: 
        number_guessing()

    elif choice == 2: 
        break

    else: 
        break

