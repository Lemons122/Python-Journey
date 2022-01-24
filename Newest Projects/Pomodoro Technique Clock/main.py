# Pomodoro Technique is a technique that should help with doing tasks efficiently. You work for 25 minutes, then take a 5 minute break. Repeat this step, and after 4 times, you take a 30 minute break.
# Minutes = Total. MinutesDisplay = Displayed Count. MinutesDisplay2 = Dummy count

import time

run = input('Start the Pomodoro cycle? (Y/N)').lower()
seconds = minutes = minutesdisplay = minutesdisplay2 = hours = pomodoros = 0
while run == 'y':
    time.sleep(1)
    seconds += 1

    if minutes == hours == 0:
        print(f'{seconds} seconds elapsed')

    if minutes > 0 and hours == 0:
        print(f'{minutesdisplay} minutes, and {seconds} seconds elapsed')
    if minutes > 0 and hours > 0:
        print(f'{hours} hours, {minutesdisplay} minutes, and {seconds} seconds elapsed')
    if seconds == 60:
        minutesdisplay += 1
        minutesdisplay2 += 1
        minutes += 5
        seconds = 0
    if minutes == 60:
        hours += 1
        minutesdisplay = 0

    if minutesdisplay2 == 25 or minutesdisplay2 == 55 or minutesdisplay2 == 85:
        print('TIME TO TAKE A BREAK FOR 5 MINUTES! (Remember, dont think about work)')

    if minutesdisplay2 == 30 or minutesdisplay2 == 60 or minutesdisplay2 == 90:
        pomodoros += 1
        print(f'Get back to work. You have completed {pomodoros} out of 4 pomodoros until your big break.')
    if minutesdisplay2 == 120:
        print('You have completed 4 out of 4 pomodoros. Take a 30 minute break!')
    if minutesdisplay2 == 150:
        print('Get back to work. You have completed 0 out of 4 pomodoros until your big break.')
        minutesdisplay = minutesdisplay2 = secondsdisplay = pomodoros = 0
