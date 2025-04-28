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