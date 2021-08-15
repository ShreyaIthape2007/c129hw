#merge data
import csv

dataset1 = []
dataset2 = []

with open('bright_stars.csv','r') as f:
    csv_reader = csv.reader(f)

    for row in csv_reader:
        dataset1.append(row)
    

with open('cleaned_dwarfs_stars.csv','r') as f:
    csv_reader = csv.reader(f)

    for row in csv_reader:
        dataset2.append(row)


print('DATASET 1 : ',dataset1)
print('DATASET 2 : ',dataset2)

header1 = dataset1[0]
header2 = dataset2[0]

planet_data1 = dataset1[1:]
planet_data2 = dataset2[1:]

headers = header1 + header2

planet_data = []

for i in planet_data1:
    planet_data.append(i)
for j in planet_data2:
    planet_data.append(j)


with open('merged_data.csv','a+') as f:
    csv_writer = csv.writer(f)

    csv_writer.writerow(headers)

    csv_writer.writerows(planet_data)
