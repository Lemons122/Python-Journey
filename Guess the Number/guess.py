import random
def guess(a):
    random_number = random.randint(1, a)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Type a number between 1 and {a}: "))
        if guess > random_number:
            print("Try guessing lower!")
        elif guess < random_number:
            print("Try guessing higher!")

    print(f'Hopefully you feel better knowing that you got the right number ({random_number})...')

def computerguess(a):
    low = 1
    high = a
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high? (H), too low? (L), or Correct? (C)").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"The number is {guess}")

computerguess(20)
guess(10)