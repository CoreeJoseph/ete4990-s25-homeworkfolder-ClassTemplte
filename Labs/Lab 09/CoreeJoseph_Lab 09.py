import random
import datetime
import os

log_levels = ["INFO", "WARNING", "ERROR", "CRITICAL"]
components = ["sqldb", "ui", "frontend.js", "backend.js"]

messages = [
    "System failure",
    "Database corruption",
    "Disk failure detected",
    "Connection timeout",
    "Unhandled exception",
    "User login successful",
    "Heartbeat ok",
    "Service restarted"
]

if not os.path.exists("Logs"):
    os.makedirs("Logs")
    

for component in components:
    filename = f"Logs/{component}.log"
    with open(filename, 'w') as file:
        for i in range(10):
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S,%f")[:-3] #ai helped me with this line
            level = random.choice(log_levels)
            message = random.choice(messages)
            file.write(f"{timestamp} | {component} | {level} | {message}\n")

print("Log files created successful.")
import re
import json

def read_log_file(filepath):
    try:
        with open(filepath, "r") as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print("Error: File not found.")
        return []

def parse_log_line(line):
    pattern = r"^(.*?)\s\|\s(.*?\s\|\s(.*?)\s\|\s(.*)$)" 
    match = re.match(pattern, line)
    if match:
        timestamp, component, level, message = match.groups()
        return timestamp, component, level, message
    else:
        return None  
    
def count_log_levels(log_lines):
    log_summary = {}

    for line in log_lines:
        parsed = parse_log_line(line)
        if parsed:
            parsed = timestamp, component, level, message 
            if level not in log_summary:
                log_summary[level] = {}
            if message not in log_summary[level]:
                log_summary[level][message] = 0
            log_summary[level][message] += 1

    return log_summary

def main():
    filepath = input("Enter the path to the log file: ")
    lines = read_log_file(filepath)

    if lines:
        summary = count_log_levels(lines)
        json_filename = "log_summary.json"

        with open(json_filename, "w") as json_file:
            json.dump(summary, json_file, indent = 4)

        print(f"Summary saved to {json_filename}")

if __name__ == "__main__":
    main()

import threading 
import time
import json
import matplotlib.pyplot as plt
import os

def monitor_json(filepath):
    seen_entries = {}

    while True:
        if os.path.exists(filepath):
            with open(filepath, "r") as file:
                data = json.load(file)
            
            counts = {level: sum(messages.values()) for level, messages in data.items()}

            print("\n--- Log Summary ---")
            for level, count in counts.items():
                print(f"{level}: {count}")

            critical_messages = data.get("CRITICAL", {})
            for message, count in critical_messages.items():
                if message not in seen_entries:
                    print(f"[CRITICAL] New critical message: {message}")
                    seen_entries[message] = count
        else:
            print("Waitng for JSON...")
        
        time.sleep(5)

def plot_graph(filepath):
    while True:
        if os.path.exists(filepath):
            with open(filepath, "r") as file:
                data = json.load(file)
            
            counts = {level: sum(messages.values()) for level, messages in data.items()}

            if counts:
                plt.clf()
                levels = list(counts.keys())
                values = list(counts.values())

                plt.bar(levels, values, color=["blue", "orange", "red", "purple"])
                plt.title("Log Levels Distribution")
                plt.xlabel("Log Level")
                plt.ylabel("Number of Messages")
                plt.pause(5)
            
            else:
                print("No data..")
        
        else:
            print("Waiting for JSON..")

        time.sleep(5)

def main():
    filepath = "log_summary.json"

    print("Select an option: ")
    print("1. Monitor JSON and print critical messages")
    print("2. Graph log level distribution")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        monitor_thread = threading.Thread(taarget=monitor_json, args=(filepath,), daemon=True)
        monitor_thread.start()
    elif choice == "2":
        plt.ion()
        graph_thread = threading.Thread(target=plot_graph, args=(filepath,), daemon=True)
        graph_thread.start()
    else:
        print("Invalid choice.")
        return
    
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()