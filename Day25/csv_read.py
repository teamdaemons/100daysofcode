import csv


# with open("weather_data2.csv") as file:
#     data = file.readlines()
#     print(data)


with open("weather_data2.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        print(row)
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
    print(temperatures)
