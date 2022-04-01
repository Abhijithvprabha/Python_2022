# with open("weather_data.csv") as weather_file:
#     data = weather_file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as weather_file:
#     data = csv.reader(weather_file)
#     temprature = []
#     for row in data:
#         if row[1] != 'temp':
#             temprature.append(int(row[1]))
#     print(temprature)

import pandas as pd

data = pd.read_csv("weather_data.csv")
print(data)
print(data['temp'])