#Write your code below this line 👇
def prime_checker(number):
  list = [1,2,3,5,7]
  count = 2
  for item in list:
    if number % item == 0:
      count = count + 1

  if count > 3:
      print("It's not a prime number.")
  else:
      print("It's a prime number.")
  




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



