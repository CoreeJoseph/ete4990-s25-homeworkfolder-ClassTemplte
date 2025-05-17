import threading
import datetime
from config import START_DATE, END_DATE, MAX_THREADS, BASE_FOLDER
from downloader import download_xml
from parser import xml_to_json
from utils import file_exists

limit = threading.Semaphore(MAX_THREADS)

def download_and_parse(date):
    date_str = date.strftime("%Y-%m-%d")
    xml_path = f"{BASE_FOLDER}/{date_str}.xml"
    json_path = f"{BASE_FOLDER}/{date_str}.json"

    if file_exists(xml_path, json_path):
        print(f"Already downloaded for {date_str}")
        return

    with limit:
        xml_file = download_xml(date)
        xml_to_json(xml_file)

def main():
    current_date = START_DATE
    threads = []
    while current_date <= END_DATE:
        threads = [t for t in threads if t.is_alive()]
        while len(threads) >= MAX_THREADS:
            threads = [t for t in threads if t.is_alive()]

        t = threading.Thread(target=download_and_parse, args=(current_date,))
        t.start()
        threads.append(t)
        current_date += datetime.timedelta(days=1)

    for t in threads:
        t.join()
    print("All downloads complete.")

if __name__ == "__main__":
    main()
