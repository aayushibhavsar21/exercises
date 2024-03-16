
print("_______greeting based on current time_______")

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hr = int(time.strftime('%H'))
print("hour:",hr)
min = int(time.strftime('%M'))
print("min:",min)
sec = int(time.strftime('%S'))
print("sec:",sec)

if hr>5 and hr < 12 :
     print('Good morning')
elif hr > 11 and hr < 16:
     print('Good afternoon')
elif hr > 15 and hr < 24 :
     print('Good evening')
else:
    print("good night")

