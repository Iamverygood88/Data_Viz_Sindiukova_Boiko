import numpy as np
import matplotlib.pyplot as plt
import csv

categories = []
Uzbekistan = []
Belarus = []


with open('data/OlympicsWinter.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:
            categories.append(row)
            line_count += 1

        else:
            if row[4] == "UZB":
                print('total medals for Uzbekistan:', len(Uzbekistan))
                Uzbekistan.append([int(row[0]), row[5], row[6], row[7]])
            elif row[4] == "BLR":
                print('total medals for Belarus:', len(Belarus))
                Belarus.append([int(row[0]), row[5], row[6], row[7]])
                line_count += 1

totalMedals = len(Uzbekistan) + len(Belarus)

Uzbekistan_procentage = int(len(Uzbekistan) / totalMedals * 100)
Belarus_procentage = int(len(Belarus) / totalMedals * 100)

print('processed', line_count, 'line of data.Total medals', totalMedals)

x = ['Belarus']
y = [Belarus_procentage]

x2 = ['Uzbekistan']
y2 = [Uzbekistan_procentage]


plt.bar(x, y, label='Belarus', color='coral')
plt.bar(x2, y2, label='Uzbekistan', color='crimson')

plt.xlabel('Countries')
plt.ylabel('Amount of Medals')

plt.title('Belarus VS Uzbekistan')
plt.legend()
plt.show()
