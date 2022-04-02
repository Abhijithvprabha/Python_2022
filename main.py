import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# print(data["Primary Fur Color"])

gray_sq_count = len(data[data["Primary Fur Color"] == 'Gray'])
print(gray_sq_count)

cina_sq_count = len(data[data["Primary Fur Color"] == 'Cinnamon'])
print(cina_sq_count)

black_sq_count = len(data[data["Primary Fur Color"] == 'Black'])
print(black_sq_count)

data_dict = {
    "Fur Color" : ["Gray" , "Cinnamon", "Black"] ,
    "Count" : [gray_sq_count, cina_sq_count, black_sq_count]
}

print(data_dict)
Df = pandas.DataFrame(data_dict)
Df.to_csv("final_sq_count")