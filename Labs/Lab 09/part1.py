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

print("Log files created successful.")