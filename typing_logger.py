# typing_logger.py
# typing recorder
# tracks every key press + release time and saves to a csv
# goal is to analyze focus / stress based on pauses and corrections

import time
import csv
import os
from datetime import datetime
from pynput import keyboard

# make a data folder if it doesnt exist yet
if not os.path.exists("data"):
    os.makedirs("data")

# figure out filename like data/session_2025-xx-xx_123412.csv
session_name = datetime.now().strftime("session_%Y-%m-%d_%H%M%S.csv")
file_path = os.path.join("data", session_name)

last_time = None  # we store time of last key press to calculate pauses

# open csv in write mode
f = open(file_path, "w", newline="", encoding="utf-8")
writer = csv.writer(f)
writer.writerow(["timestamp", "key", "event_type", "time_since_last_key"])

print("typing logger started… (press ctrl + c to stop)")
print(f"logging to file: {file_path}")
print("--------------------------------------------------------")

def on_press(key):
    global last_time
    now = time.time()

    # figure out delay since last key press
    if last_time is None:
        diff = 0
    else:
        diff = round((now - last_time) * 1000, 3)  # in ms

    last_time = now

    # try to get key as text
    try:
        k = key.char
    except:
        k = str(key)

    writer.writerow([datetime.now(), k, "down", diff])

def on_release(key):
    # log key release but without delay calc
    try:
        k = key.char
    except:
        k = str(key)

    writer.writerow([datetime.now(), k, "up", ""])

    # optional: stop if esc is pressed
    if key == keyboard.Key.esc:
        return False

try:
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
except KeyboardInterrupt:
    print("stopped.")
finally:
    f.close()
    print(f"file saved: {file_path}")
