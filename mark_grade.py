mark = int(input("what's your mark ?"))
if mark <= 90:
  if mark > 80 and mark <= 90:
    print("B")
  elif mark >= 60 and mark <= 80:
    print("C")
  else:
    print("D")
else:
  print(" A")  