from art import logo
print(logo)

#calculator

def add(n1,n2):
  return (n1+n2)


def sub(n1,n2):
  return (n1-n2)


def div(n1,n2):
  return n1/n2


def mult(n1,n2):
  return n1*n2

operations = {
  
  "*":mult,
  "+":add,
  "-":sub,
  "/":div

}

def calculator():

  number1 = int(input("What's the first number? "))
  for key in operations:
    print(key)
  continue_calc = True 
  while continue_calc:
    choose_operation = input("Pick an operation: ")
    number2 = int(input("What's the next number? "))
    function = operations[choose_operation]
    answer1 = function(number1,number2)  
    print(answer1)
    continue_calc = input(f"Type 'y' to continue with the {answer1} or 'n' for to exit: ")
    if continue_calc == "y":
      number1 = answer1
    else:
      continue_calc = False
      calculator()
      
      
calculator()
