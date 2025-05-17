import requests
from time import sleep
from config import BASE_FOLDER, BASE_CURRENCY
from utils import make_folder

def download_xml(date):
    make_folder(BASE_FOLDER)
    date_str = date.strftime("%Y-%m-%d")
    xml_path = f"{BASE_FOLDER}/{date_str}.xml"

    url = (
        f"https://www.floatrates.com/historical-exchange-rates.html?"
        f"operation=rates&pb_id=1775&page=historical&currency_date={date_str}"
        f"&base_currency_code={BASE_CURRENCY}&format_type=xml"
    )
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        with open(xml_path, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"Downloaded XML for {date_str}")
        sleep(0.3)
        return xml_path
    except Exception as e:
        print(f"Download failed for {date_str}: {e}")
        return None
