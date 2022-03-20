def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        #print("Leap year.")
        return True
      else:
        #print("Not leap year.")
        return False
    else:
      #print("Leap year.")
      return True
  else:
    return False
    #print("Not leap year.")

def days_in_month(year,month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if is_leap(year) and month == 2 :
   return 29
  else:
    return month_days[month-1]
  
  
#🚨 Do NOT change any of the code below 
year_to_check = int(input("Enter a year: "))
month_to_check = int(input("Enter a month: "))
days = days_in_month(year_to_check, month_to_check)
print(days)












