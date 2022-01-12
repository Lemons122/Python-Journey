from datetime import datetime
import pytz
import time

i = 1
eastern = pytz.timezone('US/Eastern')

while i < 10:
    datetime_booba = datetime.now(eastern)
    print("Booba's Time:", datetime_booba.strftime("%H:%M:%S"))
    time.sleep(3)
    
