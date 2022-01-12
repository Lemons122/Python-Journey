import sys
from random import sample
import time

towerval = int(input('How Many Towers Would You Like To Choose From?\n'))
if towerval > 22:
    print('Choose a value between 1-22. The program will now exit')
    time.sleep(2)
    sys.exit()

towertype = input('Primary, Military, Magic, Support, or All (You May Combine)\n').lower()
dart, boomer, bomb, tack, ice, glue, sniper, sub, buccaneer, ace, heli, mortar, dartling, wizard, super, ninja, alchemist, druid, banana, spike, village, engineer = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
towerlist = 'dart', 'boomer', 'bomb', 'tack', 'ice', 'glue', 'sniper', 'sub', 'buccaneer', 'ace', 'heli', 'mortar', 'dartling', 'wizard', 'super', 'ninja', 'alchemist', 'druid', 'banana', 'spike', 'village', 'engineer'
primary = ['dart', 'boomer', 'bomb', 'tack', 'ice', 'glue']  # 6
military = ['sniper', 'sub', 'buccaneer', 'ace', 'heli', 'mortar', 'dartling']  # 7
magic = ['wizard', 'super', 'ninja', 'alchemist', 'druid']  # 5
support = ['banana', 'spike', 'village', 'engineer']  # 4
if towertype == 'all':
    print(sample(towerlist, towerval))
    time.sleep(10800)

if towertype == 'primary':
    if towerval > 6:
        print('Choose a value between 1-6. The program will now exit')
        time.sleep(2)
        sys.exit()
    else:
        print(sample(primary, towerval))
        time.sleep(10800)

if 'primary' in towertype and 'military' in towertype and not 'magic' in towertype:
    if towerval > 13:
        print('Choose a value between 1-13. The program will now exit')
        time.sleep(2)
        sys.exit()
    else:
        primary.extend(military)
        print(sample(primary, towerval))
        time.sleep(10800)

if 'primary' in towertype and 'military' in towertype and 'magic' in towertype:
    if towerval > 18:
        print('Choose a value between 1-18. The program will now exit')
        time.sleep(2)
        sys.exit()
    else:
        primary.extend(military)
        primary.extend(magic)
        print(sample(primary, towerval))
        time.sleep(10800)

if 'primary' in towertype and 'military' in towertype and 'support' in towertype:
    if towerval > 17:
        print('Choose a value between 1-17. The program will now exit')
        time.sleep(2)
        sys.exit()
    else:
        primary.extend(military)
        primary.extend(support)
        print(sample(primary, towerval))
        time.sleep(10800)

if 'primary' in towertype and 'magic' in towertype:
    if towerval > 11:
        print('Choose a value between 1-11. The program will now exit')
        time.sleep(2)
        sys.exit()
    else:
        primary.extend(magic)
        print(sample(primary, towerval))
        time.sleep(10800)

if 'primary' in towertype and 'magic' in towertype and 'support' in towertype:
    if towerval > 17:
        print('Choose a value between 1-17. The program will now exit')
        time.sleep(2)
        sys.exit()
    else:
        primary.extend(magic)
        primary.extend(support)
        print(sample(primary, towerval))
        time.sleep(10800)

if 'primary' in towertype and 'support' in towertype:
    if towerval > 10:
        print('Choose a value between 1-10. The program will now exit')
        time.sleep(2)
        sys.exit()
    else:
        primary.extend(support)
        print(sample(primary, towerval))
        time.sleep(10800)
if towertype == 'military':
    if towerval > 7:
        print('Choose a value between 1-7. The program will now exit')
        time.sleep(2)
        sys.exit()
    else:
        print(sample(military, towerval))
        time.sleep(10800)

if 'military' in towertype and 'magic' in towertype and not 'support' in towertype:
    if towerval > 12:
        print('Choose a value between 1-12. The program will now exit')
        time.sleep(2)
        sys.exit()
    else:
        military.extend(magic)
        print(sample(military, towerval))
        time.sleep(10800)

if 'military' in towertype and 'support' in towertype and not 'magic' in towertype:
    if towerval > 11:
        print('Choose a value between 1-11. The program will now exit')
        time.sleep(2)
        sys.exit()
    else:
        military.extend(support)
        print(sample(military, towerval))
        time.sleep(10800)

if 'military' in towertype and 'magic' in towertype and 'support' in towertype:
    if towerval > 16:
        print('Choose a value between 1-16. The program will now exit')
        time.sleep(2)
        sys.exit()
    else:
        military.extend(magic)
        military.extend(support)
        print(sample(military, towerval))
        time.sleep(10800)

if towertype == 'magic':
    if towerval > 5:
        print('Choose a value between 1-5. The program will now exit')
        time.sleep(2)
        sys.exit()
    else:
        print(sample(magic, towerval))
        time.sleep(10800)
if 'magic' in towertype and 'support' in towertype:
    if towerval > 9:
        print('Choose a value between 1-9. The program will now exit')
        time.sleep(2)
        sys.exit()
    else:
        magic.extend(support)
        print(sample(magic, towerval))
        time.sleep(10800)
if towertype == 'support':
    if towerval > 4:
        print('Choose a value between 1-4. The program will now exit')
        time.sleep(2)
        sys.exit()
    else:
        print(sample(support, towerval))
        time.sleep(10800)
