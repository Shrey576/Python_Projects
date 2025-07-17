import time

def countdown_timer(seconds):
    is_time_up = False  # Boolean flag to indicate if time is up

    while not is_time_up:
        if seconds > 0:
            mins, secs = divmod(seconds, 60)
            time_format = '{:02d}:{:02d}'.format(mins, secs)
            print(time_format, end='\\r')
            time.sleep(1)
            seconds -= 1
        else:
            is_time_up = True  # Time is up when seconds reach 0

    print("Time's up!")

def main():
    seconds = int(input("Enter time in seconds: "))
    countdown_timer(seconds)

main()
