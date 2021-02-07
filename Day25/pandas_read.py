import pandas

data = pandas.read_csv("weather_data2.csv")
print(data)

print(data["temp"])
for item in data["temp"]:
    print(item)


# To dictionary
data_dict = data.to_dict()
print(data_dict)

# To list
data_list = data["temp"].to_list()
print(data_list)
# average of a list
print("Average is : ", sum(data_list)/len(data_list))
print("Average is :", data["temp"].mean())
print("Maximum temperature is:", data["temp"].max())
# Get Data in columns
print(data["condition"])
print(data.condition)

# Get data in ROW
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])
monday = data[data.day == "Monday"]
print(monday.condition)  # condition on Monday
print((monday.temp * 9/5) + 32) # get temperature of Monday in Fahrenheit

# Create dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")



