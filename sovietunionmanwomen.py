import csv
import matplotlib.pyplot as plt

categories = []
Soviet_Union = []
world = []

with open('data/OlympicsWinter.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:
            categories.append(row)
            line_count += 1
        elif row[4] == "URS":
            Soviet_Union.append([int(row[0]), row[5], row[6], row[7]])

        else:
            world.append([int(row[0]), row[5], row[6], row[7]])

    print('total medals for Soviet Union:', len(Soviet_Union))
    print("total medals for everyone else:", len(world))

    print('processed', line_count, 'rows of data')

men = []
women = []

for medal in Soviet_Union:
    if medal[1] == "Men":
       men.append(medal)

for medal in Soviet_Union:
    if medal[1] == "Women":
       women.append(medal)


print('men won', len(men), 'gold medals in 1956')
print('women won', len(women), 'gold medals in 1956')
print('men won', len(men), 'gold medals in 1960')
print('women won', len(women), 'gold medals in 1960')
print('men won', len(men), 'gold medals in 1972')
print('women won', len(women), 'gold medals in 1972')
print('men won', len(men), 'gold medals in 1980')
print('women won', len(women), 'gold medals in 1980')
print('men won', len(men), 'gold medals in 1988')
print('women won', len(women), 'gold medals in 1988')

totalMedals = len(men) + len(women)

men_procentage = int(len(men) / totalMedals * 100)
women_procentage = int(len(women) / totalMedals * 100)

print('processed', line_count, 'line of data.Total medals', totalMedals)

labels = "Men", "Women", 
sizes = [men_procentage, women_procentage,]
colors = ['Lightblue', 'Pink']
explode = (0.1, 0.1)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("Medals won")
plt.xlabel("Medal Count from 1956 Men vs Women")
plt.show()
