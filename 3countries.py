import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.ticker import namedtuple
from collections import namedtuple
import csv

categories = []
Ukraine = []
Belarus = []
Uzbekistan = []

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
			if row[4] == 'UZB':
				print('total medals for Uzbekistan:', len(Uzbekistan))
				Uzbekistan.append([int(row[0]), row[5], row[6], row[7]])
				line_count += 1

totalMedals = len(Ukraine) + len(Belarus) + len(Uzbekistan)

Ukraine_procentage = int(len(Ukraine) / totalMedals * 100)
Belarus_procentage = int(len(Belarus) / totalMedals * 100)
Uzbekistan_procentage = int(len(Uzbekistan) / totalMedals * 100)

print('processed', line_count, 'line of data.Total medals', totalMedals)

x2 = ['Ukraine']
y2 = [Ukraine_procentage]

x3 = ['Belarus']
y3 = [Belarus_procentage]

x4 = ['Uzbekistan']
y4 = [Uzbekistan_procentage]

plt.bar(x2, y2, label='Ukraine', color='gold')
plt.bar(x3, y3, label='Belarus', color='chocolate')
plt.bar(x, y, label='Uzbekistan', color='teal')

plt.xlabel('Countries')
plt.ylabel('Amount of Medals')
plt.title('Ukraine VS Belarus VS Uzbelistan')
plt.legend()
plt.show()
