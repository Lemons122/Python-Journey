# Fizz buzz is a game where every multiple of 3 is replace by "Fizz" and every multple of 5 is replace by "Buzz" if something is a multiple of 3 and 5, it will be "FizzBuzz"

for i in range(1, 101):
    if (i % 3 == 0):
        if (i % 5 == 0):
            print('FizzBuzz')
        else:
            print('Fizz')
    elif (i % 5 == 0):
        print('Buzz')
    else:
        print(i)