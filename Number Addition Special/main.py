import time

number_from = float(input('Starting number: '))
number_addition = float(input('Number to add each time: '))
number_to = int(input('How many times to add the previous number: '))
number_amount1 = 0
number_amount2 = number_from
total = number_from
start_time = time.time()
print(number_from)
while number_amount1 != number_to:
    number_amount2 = number_amount2 + number_addition
    number_amount1 = number_amount1 + 1
    print("{}, {} left".format(number_amount2, number_to - number_amount1))
    assert isinstance(number_amount2, object)
    total += number_amount2

totaltime = time.time() - start_time
totaltime2 = (int(totaltime * 100)) / 100.0
print('The combined total is: {}, and completed in: {} seconds'.format(total, totaltime2))
time.sleep(60)
