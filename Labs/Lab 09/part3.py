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