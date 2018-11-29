import numpy as np 
import matplotlib.pyplot as plt
import csv

categories = []
Ukraine = []
Belarus = []

with open('data/OlympicsWinter.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:
            categories.append(row)
            line_count += 1  
        else:
            if row[4] == 'UKR':
                print('total medals for Ukraine:', len(Ukraine))
                Ukraine.append([int(row[0]), row[5], row[6], row[7]])
            elif row[4] == 'BLR':
                print('total medals for Belarus:', len(Belarus))
                Belarus.append([int(row[0]), row[5], row[6], row[7]])
                line_count += 1

totalMedals = len(Ukraine) + len(Belarus)

Ukraine_procentage = int(len(Ukraine) / totalMedals * 100)
Belarus_procentage = int(len(Belarus) / totalMedals * 100)

print('processed', line_count, 'line of data.Total medals', totalMedals)

x2 = ['Ukraine']
y2 = [Ukraine_procentage]

x3 = ['Belarus']
y3 = [Belarus_procentage]

plt.bar(x2, y2, label='Ukraine', color='tomato')
plt.bar(x3, y3, label='Belarus', color='darkorange')

plt.xlabel('Countries')
plt.ylabel('Amount of Medals')
plt.title('Belarus VS Ukraine')
plt.legend()
plt.show()
