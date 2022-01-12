import random
import time

roll_count1 = int(input('How Many Rolls? '))
roll_count2 = 0
addroll_count = 1
total = 0
random1 = 0
random2 = 0
tworolled, threerolled, fourrolled, fiverolled, sixrolled, sevenrolled, eightrolled, ninerolled, tenrolled, elevenrolled, twelverolled, tworolledpercent, threerolledpercent, fourrolledpercent, fiverolledpercent, sixrolledpercent, sevenrolledpercent, eightrolledpercent, ninerolledpercent, tenrolledpercent, elevenrolledpercent, twelverolledpercent = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
while not (roll_count2 == roll_count1):
    random1 = random.randint(1, 6)
    random2 = random.randint(1, 6)
    roll_total = random1 + random2
    if roll_total == 2:
        roll_count1 -= addroll_count
        tworolled += addroll_count
        total += addroll_count
    if roll_total == 3:
        roll_count1 -= addroll_count
        threerolled += addroll_count
        total += addroll_count
    if roll_total == 4:
        roll_count1 -= addroll_count
        fourrolled += addroll_count
        total += addroll_count
    if roll_total == 5:
        roll_count1 -= addroll_count
        fiverolled += addroll_count
        total += addroll_count
    if roll_total == 6:
        roll_count1 -= addroll_count
        sixrolled += addroll_count
        total += addroll_count
    if roll_total == 7:
        roll_count1 -= addroll_count
        sevenrolled += addroll_count
        total += addroll_count
    if roll_total == 8:
        roll_count1 -= addroll_count
        eightrolled += addroll_count
        total += addroll_count
    if roll_total == 9:
        roll_count1 -= addroll_count
        ninerolled += addroll_count
        total += addroll_count
    if roll_total == 10:
        roll_count1 -= addroll_count
        tenrolled += addroll_count
        total += addroll_count
    if roll_total == 11:
        roll_count1 -= addroll_count
        elevenrolled += addroll_count
        total += addroll_count
    if roll_total == 12:
        roll_count1 -= addroll_count
        twelverolled += addroll_count
        total += addroll_count

print(total)
print(tworolled, threerolled, fourrolled, fiverolled, sixrolled, sevenrolled, eightrolled, ninerolled, tenrolled, elevenrolled, twelverolled)
total1 = total
tworolledpercent1 = tworolled / total1
tworolledpercent = (float(tworolledpercent1 * 100)) 
threerolledpercent1 = threerolled / total1
threerolledpercent = (float(threerolledpercent1 * 100)) 
fourrolledpercent1 = fourrolled / total1
fourrolledpercent = (float(fourrolledpercent1 * 100)) 
fiverolledpercent1 = fiverolled / total1
fiverolledpercent = (float(fiverolledpercent1 * 100)) 
sixrolledpercent1 = sixrolled / total1
sixrolledpercent = (float(sixrolledpercent1 * 100))
sevenrolledpercent1 = sevenrolled / total1
sevenrolledpercent = (float(sevenrolledpercent1 * 100)) 
eightrolledpercent1 = eightrolled / total1
eightrolledpercent = (float(eightrolledpercent1 * 100)) 
ninerolledpercent1 = ninerolled / total1
ninerolledpercent = (float(ninerolledpercent1 * 100)) 
tenrolledpercent1 = tenrolled / total1
tenrolledpercent = (float(tenrolledpercent1 * 100)) 
elevenrolledpercent1 = elevenrolled / total1
elevenrolledpercent = (float(elevenrolledpercent1 * 100)) 
twelverolledpercent1 = twelverolled / total1
twelverolledpercent = (float(twelverolledpercent1 * 100)) 
print(
    'You Rolled The Dice A Total Of {} Times, With ({}) 2s ({}%), ({}) 3s ({}%), ({}) 4s ({}%), ({}) 5s ({}%), ({}) 6s ({}%), ({}) 7s ({}%), ({}) 8s ({}%), ({}) 9s ({}%), ({}) 10s ({}%), ({}) 11s ({}%), ({}) 12s ({}%)'.format(
        total, tworolled, tworolledpercent, threerolled,
        threerolledpercent, fourrolled,
        fourrolledpercent, fiverolled, fiverolledpercent,
        sixrolled, sixrolledpercent, sevenrolled,
        sevenrolledpercent, eightrolled,
        eightrolledpercent, ninerolled,
        ninerolledpercent, tenrolled, tenrolledpercent,
        elevenrolled, elevenrolledpercent, twelverolled,
        twelverolledpercent))
time.sleep(600)
