import random
import csv
from datetime import datetime, timedelta

# Veri seti oluşturma parametreleri
years = range(2010, 2025)
month = 7
high_temp_range = (25, 35)  # Temmuz ayı yüksek sıcaklıkları
low_temp_range = (15, 25)  # Temmuz ayı düşük sıcaklıkları

# CSV dosyası yazma
with open('temperatures.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "High_Temperature_C", "Low_Temperature_C"])

    for year in years:
        start_date = datetime(year, month, 1)
        for day in range(31):
            date = start_date + timedelta(days=day)
            high_temp = round(random.uniform(*high_temp_range), 1)
            low_temp = round(random.uniform(*low_temp_range), 1)
            writer.writerow([date.strftime("%Y-%m-%d"), high_temp, low_temp])

