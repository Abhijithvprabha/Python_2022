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
if bmi < 18:
  print(f"your bmi is {bmi}, you are underweight")
elif bmi <= 25:
  print(f"your bmi is {bmi}, you are normal weight")
elif bmi <= 30 :
  print(f"you are bmi is {bmi}, you are slightly overweight")
elif bmi <= 35 :
  print(f"your bmi is {bmi}, you are obese")
else:
  print(f"your bmi is {bmi}, you are clinically obese")

# print(type(bmi))








