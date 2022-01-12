from datetime import datetime
import pytz
import time

i = 1
eastern = pytz.timezone('US/Eastern')

while i < 10:
    datetime_test = datetime.now(eastern)
    print("Eastern Time:", datetime_test.strftime("%H:%M:%S"))
    time.sleep(3)
    
