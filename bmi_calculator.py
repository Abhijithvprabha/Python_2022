# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# print(type(height))
# BMI = mass / (height**height)
height = float(height)
weight = int(weight)
bmi = weight / height ** 2
bmi = round(bmi)
print(bmi)

# print(type(bmi))








