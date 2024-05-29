import csv
import pandas

# # with open("./weather_data.csv") as f:
# #     data = csv.reader(f)
# #     temperatures = []
# #     for row in data:
# #         print(row)
#
# data = pandas.read_csv("weather_data.csv")
# # print(data)
# # print(data["temp"])
#
# # data_dict = data.to_dict()
# # avg_temp = data["temp"].mean()
# # print(avg_temp)
#
# # monday = data[data.temp == data.temp.max()]
# # print(monday)
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data2 = pandas.DataFrame(data_dict)
# print(data2)

#we need to calculate how many squirrels of which color ther are in the file

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240423.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

print(data_dict)

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_cnt")

