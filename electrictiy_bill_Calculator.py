print("Welcome to Electricity bill calculator")
unit = int(input("Enter the number of units you have used? "))
bill = 0
if unit > 100:
  if unit < 200:
    bill = (unit-100) * 5
    print(f"your bill is {bill}")
  else:
    bill = 500 + (unit - 200) * 10
    print(f"your bill is {bill}")
else:
 print(" Your bill is zero")