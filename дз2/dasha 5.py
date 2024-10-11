import csv
import matplotlib.pyplot as plt
import numpy as np
from datetime import date

time, close = [], []

with open("BTC_data.csv","r") as data_file:
    data_reader = csv.reader(data_file, delimiter=",")

    for row in data_reader:
        if row[0] != "time":
            year = int(row[0][:4])
            month = int(row[0][5:7])
            day = int(row[0][8:10])
            time.append(date(year, month, day))
            close.append(int(row[4]))

    plt.title("BTC price VS Time", fontsize=15)
    plt.xlabel("Time, days")
    plt.ylabel("BTC price, u.e.")
    plt.plot(time, close, c='k')
    plt.tick_params(axis='x', labelrotation=90)
    plt.tight_layout()
    plt.savefig("BTC price VS Time.png")