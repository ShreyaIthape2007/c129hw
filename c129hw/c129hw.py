import csv

data = []

with open('dwarf_stars.csv','r') as f:
    csv_reader = csv.reader(f)

    for i in csv_reader:
        data.append(i)


headers = data[0]

stars_data = data[1:]

print('HEADERS : ',headers)
print('STARS_DATA : ',stars_data)

for i in stars_data:
    if i[3] == '' or i[4]=='':
        continue
    else: 
        i[3] = float(i[3]) * 0.000954588
        i[4] = float(i[4]) * 0.102763

print('NEW STARS DATA : ',stars_data)


with open('cleaned_dwarfs_stars.csv','a+') as f:
    csv_writer = csv.writer(f)

    csv_writer.writerow(headers)

    csv_writer.writerows(stars_data)


