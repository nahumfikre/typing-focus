# analyze_session.py
# reads one of the csv logs and tries to measure:
# - avg key delay
# - longest pause
# - how many backspaces
# - rough focus score (totally made up but good enough)

import csv
import sys
import statistics as stats

if len(sys.argv) < 2:
    print("usage: python analyze_session.py path/to/session.csv")
    sys.exit()

file_path = sys.argv[1]

delays = []
backspaces = 0
total_keys = 0

with open(file_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total_keys += 1

        # count backspaces separately for stress
        if "backspace" in row["key"].lower():
            backspaces += 1

        # only care about press events for timing
        if row["event_type"] == "down" and row["time_since_last_key"]:
            try:
                delays.append(float(row["time_since_last_key"]))
            except:
                pass

if not delays:
    print("no key data??")
    sys.exit()

avg_delay = round(stats.mean(delays), 2)
max_pause = round(max(delays), 2)
backspace_rate = round(backspaces / total_keys * 100, 2)

# rough scoring system
# lower delay + fewer corrections = higher focus
focus_score = 100 - (avg_delay / 10) - backspace_rate
focus_score = round(max(0, focus_score), 2)

print("\n----- Typing Session Results -----")
print(f"file analyzed: {file_path}")
print(f"total keys: {total_keys}")
print(f"average key delay: {avg_delay} ms")
print(f"longest pause: {max_pause} ms")
print(f"backspace rate: {backspace_rate}%")
print(f"focus score (0-100): {focus_score}")
print("----------------------------------")
