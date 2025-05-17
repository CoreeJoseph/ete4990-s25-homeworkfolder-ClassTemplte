import requests
import xmltodict
import json
import random
import os
import datetime
import threading
from time import sleep
import random
#dict to choose which currency to randomly choose from
rates = ["EUR", "GBP", "USD", "DZD", "AUD", "BWP", "BND", "CAD", "CLP", "CNY", "COP", "CZK", "DKK", "HUF", "ISK", "INR", "IDR","ILS", "KZT", "KRW", "KWD", "LYD", "MYR", "MUR", "NPR", "NZD", "NOK", "OMR", "PKR", "PLN", "QAR", "RUB", "SAR", "SGD", "ZAR", "LKR", "SEK", "CHF", "THB", "TTD"]
rates_for_base = [r for r in rates if r not in ["USD", "EUR", "GBP"]]
base_currency = random.choice(rates_for_base)
print(f"Select base currency: {base_currency}")
#limiting the amount of threads
limit = threading.Semaphore(10)
#telling which dates to pull from
start_date = datetime.date(2011, 5, 4)
end_date = datetime.date.today()
#download data both xml then turning it into json
def download_and_save(date):
    date_str = date.strftime("%Y-%m-%d")
    folder = os.path.join("data", base_currency)
    os.makedirs(folder, exist_ok=True)
    xml_path = os.path.join(folder, f"{date_str}.xml")
    json_path = os.path.join(folder, f"{date_str}.json")

    if os.path.exists(xml_path) and os.path.exists(json_path):
        print(f"Already has been downloaded and converted for {date_str}")
        return

    with limit:
        try:
            url = (f"https://www.floatrates.com/historical-exchange-rates.html?"
                   f"operation=rates&pb_id=1775&page=historical&currency_date={date_str}"
                   f"&base_currency_code={base_currency}&format_type=xml")
            response = requests.get(url, timeout = 10)
            response.raise_for_status()

            with open(xml_path, "w", encoding = "utf-8") as f_xml:
                f_xml.write(response.text)

            data_dict = xmltodict.parse(response.text)
            json_data = json.dumps(data_dict, indent = 4)
            with open(json_path, "w", encoding = "utf-8") as f_json:
                f_json.write(json_data)
            
            print(f"Download and saved {date_str}")

            sleep(0.3)

        except Exception as e:
            print(f"Failed for {date_str}: {e}")
            def main():
    current_date = start_date
    threads = []
    while current_date <= end_date:
        threads = [t for t in threads if t.is_alive()]
        while len(threads) >= 10:
            sleep(0.2)
            threads = [t for t in threads if t.is_alive()]
        t = threading.Thread(target=download_and_save, args = (current_date,))
        t.start()
        threads.append(t)
        current_date += datetime.timedelta(days = 1)

    for t in threads:
        t.join()
    print("All downloads complete..")
if __name__ == "__main__":
    main() 