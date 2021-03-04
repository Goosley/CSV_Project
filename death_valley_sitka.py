import csv
from datetime import datetime

open_death_valley = open("death_valley_2018_simple.csv", "r")
open_sitka = open("sitka_weather_2018_simple.csv", "r")

csv_death_valley = csv.reader(open_death_valley, delimiter=",")
csv_sitka = csv.reader(open_sitka, delimiter=",")

header_row = next(csv_death_valley)
header_row = next(csv_sitka)

for index, column_header in enumerate(header_row):
    print("Index:", index, "Column Name:", column_header)

highs_death = []
dates_death = []
lows_death = []

highs_sitka = []
dates_sitka = []
lows_sitka = []

for row in csv_death_valley:
    try:
        high_d = int(row[4])
        low_d = int(row[5])
        converted_date_d = datetime.strptime(row[2], "%Y-%m-%d")
    except ValueError:
        print(f"missing data for {converted_date_d}")
    else:
        highs_death.append(high_d)
        lows_death.append(low_d)
        dates_death.append(converted_date_d)

for row in csv_sitka:
    try:
        high_s = int(row[5])
        low_s = int(row[6])
        converted_date_s = datetime.strptime(row[2], "%Y-%m-%d")
    except ValueError:
        print(f"missing data for {converted_date_s}")
    else:
        highs_sitka.append(high_s)
        lows_sitka.append(low_s)
        dates_sitka.append(converted_date_s)

# print(highs)

import matplotlib.pyplot as plt

fig, axis = plt.subplots(2)

axis[0].plot(dates_sitka, highs_sitka, c="red", alpha=0.5)
axis[0].plot(dates_sitka, lows_sitka, c="blue", alpha=0.5)
axis[1].plot(dates_death, highs_death, c="red", alpha=0.5)
axis[1].plot(dates_death, lows_death, c="blue", alpha=0.5)

axis[0].set_title(
    "Temperature Comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US\n\nSITKA AIRPORT, AK US"
)

plt.title("SITKA AIRPORT, AK US", fontsize=12)
plt.xlabel("", fontsize=12)

plt.title("DEATH VALLEY, CA US", fontsize=12)
plt.xlabel("", fontsize=12)

axis[1].fill_between(dates_death, highs_death, lows_death, facecolor="blue", alpha=0.1)
plt.tick_params(axis="both", labelsize=12)

axis[0].fill_between(dates_sitka, highs_sitka, lows_sitka, facecolor="blue", alpha=0.1)
plt.tick_params(axis="both", labelsize=12)

fig.autofmt_xdate()

plt.show()
