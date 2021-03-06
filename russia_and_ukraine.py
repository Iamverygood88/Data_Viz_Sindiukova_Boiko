import numpy as np
import matplotlib.pyplot as plt
import csv

categories = []
Russia = []
Ukraine = []

with open('data/OlympicsWinter.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:
            categories.append(row)
            line_count += 1

        else:
            if row[4] == "RUS":
                print('total medals for Russia:', len(Russia))
                Russia.append([int(row[0]), row[5], row[6], row[7]])
            elif row[4] == "UKR":
                print('total medals for Ukraine:', len(Ukraine))
                Ukraine.append([int(row[0]), row[5], row[6], row[7]])
                line_count += 1

totalMedals = len(Russia) + len(Ukraine)

Russia_procentage = int(len(Russia) / totalMedals * 100)
Ukraine_procentage = int(len(Ukraine) / totalMedals * 100)

print('processed', line_count, 'line of data.Total medals', totalMedals)

x = ['Russia']
y = [Russia_procentage]

x2 = ['Ukraine']
y2 = [Ukraine_procentage]


plt.bar(x, y, label='Russia', color='dodgerblue')
plt.bar(x2, y2, label='Ukraine', color='yellow')

plt.xlabel('Countries')
plt.ylabel('Amount of Medals')
plt.title('Russia VS Ukraine')
plt.legend()
plt.show()
