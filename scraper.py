import os
import requests
import csv
import time
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import schedule

CSV_FILE = "daily_data.csv"

def get_horoscope_by_day(zodiac_sign: int, day: str, date_str: str = None):
    if date_str:
        url = f"https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign={zodiac_sign}&laDate={date_str.replace('-', '')}"
    else:
        url = f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-{day}.aspx?sign={zodiac_sign}"
    
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

def check_missing_dates():
    start_date = datetime(2024, 1, 1)
    end_date = datetime.now() - timedelta(days=1)
    
    all_dates = set((start_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in range((end_date - start_date).days + 1))
    
    existing_dates = set()
    if os.path.isfile(CSV_FILE):
        with open(CSV_FILE, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                existing_dates.add(row['Date'])
    
    missing_dates = sorted(all_dates - existing_dates)
    return missing_dates

def scrape_missing_data(missing_dates):
    if not missing_dates:
        return
    
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

    data_to_save = []
    for date_str in missing_dates:
        for sign, zodiac_num in ZODIAC_SIGNS.items():
            horoscope = get_horoscope_by_day(zodiac_num, day=None, date_str=date_str)
            if horoscope:
                data_to_save.append({
                    'Date': date_str,
                    'Zodiac Sign': sign,
                    'Horoscope': horoscope
                })
                print(f"Horoscope for {sign} on {date_str} saved successfully.")
            else:
                print(f"Could not retrieve horoscope for {sign} on {date_str}.")

    save_to_csv(data_to_save)
    print("\nMissing data saved to CSV.")

def scrape_and_store():
    missing_dates = check_missing_dates()
    if missing_dates:
        print(f"Missing data detected for dates: {missing_dates}")
        scrape_missing_data(missing_dates)
    else:
        print("No missing data detected.")
    
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
    schedule.every().day.at("10:29").do(scrape_and_store)

    while True:
        schedule.run_pending()
        time.sleep(60)
