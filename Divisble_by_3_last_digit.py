number = int(input("Enter the number "))
last_digit = number % 10
if last_digit % 3 == 0:
  print("divisble by 3")
else:
  print("not divisble by 3")