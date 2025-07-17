import time
from datetime import datetime

def alarm_clock(alarm_time):
    is_alarm_triggered = False  # Boolean flag to check if alarm is triggered

    while not is_alarm_triggered:
        current_time = datetime.now().strftime("%H:%M")
        print(f"Current Time: {current_time}", end='\\r')
        if current_time == alarm_time:
            print("\\nTime's up! Alarm ringing!")
            is_alarm_triggered = True  # Set to True when alarm time is reached
        time.sleep(30)

def main():
    alarm_time = input("Enter the time for the alarm (HH:MM): ")
    alarm_clock(alarm_time)

main()
