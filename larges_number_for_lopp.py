# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
#print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
largest_number = 0
for number in student_scores: 
  if number > largest_number:
    largest_number = number
  else:
     largest_number = largest_number

print(f"The highest score in the class is: {largest_number}")
  




