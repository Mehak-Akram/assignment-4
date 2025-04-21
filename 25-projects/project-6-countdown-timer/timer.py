#python project 5
#CountDown Timer

import time

def countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        time_format = '⏳ {:02d}:{:02d} ⏳'.format(mins, secs)
        print(time_format, end='\r')
        time.sleep(1)
        seconds -= 1
    print("⏰ 00:00 Time's Up! 🚀")

# Get user input
total_sec = int(input("Enter Time in Seconds for Countdown Timer ⏲️: "))
countdown(total_sec)
