import datetime
import pyautogui
import sys
import time

def wide_awake(seconds):
    try:
        print("Starting to keep awake. Use ctrl + C to exit.")
        print("Simulating ctrl key press every {} seconds".format(seconds))
        print("Start time: " + str(datetime.datetime.now()))
        while True:
            time.sleep(seconds)
            pyautogui.hotkey("ctrl")
            time.sleep(seconds)
            pyautogui.hotkey("ctrl")
    except KeyboardInterrupt:
        print("User terminated program")
        print("End time: " + str(datetime.datetime.now( )))
        sys.exit()

def print_usage():
    print("Usage:")
    print("python caffeine.py [seconds]")
    print("seconds: time to elapse between movement of mouse cursor")

if len(sys.argv) == 1:
    seconds = 60
elif len(sys.argv) == 2:
    try:
        seconds = int(sys.argv[1])
    except:
        print("Use integer as argument\n\n")
        print_usage()
        sys.exit()
elif len(sys.argv) > 2:
    print_usage()
    sys.exit()

wide_awake(seconds)