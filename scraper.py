import os
import requests
import csv
import time
import webbrowser
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import schedule

CSV_FILE = "daily_data.csv"

def get_horoscope_by_day(zodiac_sign: int, day: str, date_str: str = None):
    if date_str:
        url = f"https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign={zodiac_sign}&laDate={date_str.replace('-', '')}"
    else:
        url = f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-{day}.aspx?sign={zodiac_sign}"
    
    webbrowser.open(url)
    time.sleep(2)
    
    res = requests.get(url)
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, 'html.parser')
        data = soup.find('div', attrs={'class': 'main-horoscope'})
        return data.p.text if data else None
    return None

def save_to_csv(data):
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Date', 'Zodiac Sign', 'Horoscope'])
        if not file_exists:
            writer.writeheader()  
        for row in data:
            writer.writerow(row)

def scrape_and_store():
    ZODIAC_SIGNS = {
        "Aries": 1,
        "Taurus": 2,
        "Gemini": 3,
        "Cancer": 4,
        "Leo": 5,
        "Virgo": 6,
        "Libra": 7,
        "Scorpio": 8,
        "Sagittarius": 9,
        "Capricorn": 10,
        "Aquarius": 11,
        "Pisces": 12
    }

    day = "today" 
    data_to_save = []
    for sign, zodiac_num in ZODIAC_SIGNS.items():
        horoscope = get_horoscope_by_day(zodiac_num, day)
        if horoscope:
            data_to_save.append({
                'Date': datetime.now().strftime('%Y-%m-%d'),
                'Zodiac Sign': sign,
                'Horoscope': horoscope
            })
            print(f"Horoscope for {sign} saved successfully.")
        else:
            print(f"Could not retrieve horoscope for {sign}.")

    save_to_csv(data_to_save)
    print("\nData saved to CSV.")

if __name__ == "__main__":
    schedule.every().day.at("18:35").do(scrape_and_store)

    while True:
        schedule.run_pending()
        time.sleep(60)
