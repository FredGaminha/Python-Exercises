import time

def countdown(userTime):
    while userTime:
        mins, secs = divmod(userTime, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end = "\r")
        time.sleep(1)
        userTime -= 1
    return

userTime = input("Type a time in seconds: ")

countdown(int(userTime))