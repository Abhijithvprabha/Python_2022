
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#TRUE
#LOVE
name1 = name1.lower()
name2 = name2.lower()
total_name = name1 + name2
count_T = total_name.count("t")
count_R = total_name.count("r")
count_U = total_name.count("u")
count_L = total_name.count("l")
count_O = total_name.count("o")
count_V = total_name.count("v")
count_E = total_name.count("e")

first_digit_of_percentage = count_T + count_R + count_U + count_E
second_digit_of_percentage = count_L + count_O + count_V + count_E

total_percentage = str(first_digit_of_percentage) + str(second_digit_of_percentage)

final_total_percentage = int(total_percentage)

if final_total_percentage < 10 or final_total_percentage > 90 :
  print(f'"Your score is {final_total_percentage}, you go together like coke and mentos."')
elif final_total_percentage > 40 and final_total_percentage < 50 :
  print(f'Your score is {final_total_percentage}, you are alright together.')
else:
  print(f'"Your score is {final_total_percentage}."')
