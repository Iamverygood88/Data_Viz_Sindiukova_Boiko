import csv
import matplotlib.pyplot as plt

categories = []
Soviet_Union = []
Canada = []


with open('data/OlympicsWinter.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0


    for row in reader:
        if line_count is 0:
            categories.append(row)
            line_count += 1

        else:
            if row[4] == "URS":
                print('total medals for Soviet Union:', len(Soviet_Union))
                Soviet_Union.append([int(row[0]), row[5], row[6], row[7]])
            elif row[4] == "CAN":
                print('total medals for Canada:', len(Canada))
                Canada.append([int(row[0]), row[5], row[6], row[7]])
                line_count += 1

totalMedals = len(Soviet_Union) + len(Canada)

Soviet_procentage = int(len(Soviet_Union) / totalMedals * 100)
Canada_procentage = int(len(Canada) / totalMedals * 100)

print('processed', line_count, 'line of data.Total medals', totalMedals)

labels = "Soviet_Union", "Canada", 
sizes = [Soviet_procentage, Canada_procentage,]
colors = ['Red', 'Brown']
explode = (0.1, 0.1)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("Medals battle")
plt.xlabel("Medals Soviet Union VS Canada")
plt.show()
