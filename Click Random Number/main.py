import pynput
import random
import time

minimum = int(input('Minimum: '))
maximum = int(input('Maximum: '))
print('Click to see a random number')


def on_click(x, y, button, pressed):
    time.sleep(1)
    random_number = random.randrange(minimum, maximum)
    print('Your random number is: {0}. \nClick again to see another random number'.format(random_number))


with pynput.mouse.Listener(on_click=on_click) as listener:
    listener.join()
