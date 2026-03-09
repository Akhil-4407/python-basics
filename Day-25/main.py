import csv
data = []
with open("./weather_data.csv") as file:
    data = csv.reader(file)
    temperatures = []
    x = 0
    for i in data:
        if x>0:
            temp = int(i[1])
            temperatures.append(temp)
        else:
            x+=1
    print(temperatures)
import pandas
data = pandas.read_csv("weather_data.csv")
print(data)
print(data.to_dict())
teamp_list = data["temp"].to_list()
print(teamp_list)
print(data["temp"].mean())
print(data[data.day == "Monday"])
print(data[data.temp == data["temp"].max()])
monday = data[data.day == "Monday"]
print(monday.temp)
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color_list = data["Primary Fur Color"].to_list()
print(color_list)
data_dict = {
    "Color": ["Gray","Cinnamon","Black"],
    "Count":[color_list.count("Gray"),color_list.count("Cinnamon"),color_list.count("Black")]
    }
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("new_data.csv")
