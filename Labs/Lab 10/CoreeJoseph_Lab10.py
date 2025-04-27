import docker
import time 
from datetime import datetime, timedelta

client = docker.from_env()

CONTAINER_NAMES = ['lab10_container1', 'lab10_container2']

last_restart_time = {name: datetime.now() for name in CONTAINER_NAMES}

def check_container_status(containers_name):
    try:
        container = client.containers.get(containers_name)

        if container.status == 'running':
            ip_address = container.attrs['NetworkSettings']['IPAddress']
            print(f"{containers_name} is running at IP: {ip_address}")
        
        else: 
            print(f"{containers_name} is not running. Trying to restart...")
            container.start()
    except docker.errors.NotFound:
        print(f"Container {containers_name} not found.")

def maintenance_restart(container_name):
    try:
        now = datetime.now()
        if now - last_restart_time[container_name] > timedelta(days=1):
            container = client.comntainers.get(container_name)
            print(f"Performing restart on {container_name}...")
            container.restart()
            last_restart_time[container_name] = datetime.now
    except docker.errors.NotFound:
        print(f"Container {container_name} not found for restart.")

def main():
    while True:
        for containers_name in CONTAINER_NAMES:
            check_container_status(containers_name)
            #maintenance_restart(containers_name)

        print("\nWaiting 1 minute before checking again...\n")
        time.sleep(30)
if __name__ == "__main__":
    main()