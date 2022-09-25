from time import sleep
from os import system

def format(seconds):
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    return '%d:%02d:%02d' % (hour, min, sec)

seconds = 0
while True:
    print(format(seconds))
    sleep(1)
    seconds += 1
    system('clear')
