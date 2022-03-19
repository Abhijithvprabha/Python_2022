from replit import clear
from art import logo
print(logo)
#HINT: You can call clear() to clear the output in the console.
def auction():
  name_of_bidder = input("what is your name?: ")
  bid_value = int(input("what's your bid? $"))
  
  bids[name_of_bidder] = bid_value
  #print(bids)
  more_bids = input("Are there any other bidders? Tye 'yes' or 'no.' ").lower()
  if more_bids == "yes":
    clear()
    auction()
  else:
    clear()
    value = 0
    highest_bidder =""
    for name in bids:
      if bids[name] >= value:
        value = bids[name]
        highest_bidder = name
      # else:
      #   value
    #print(value)
    #print(highest_bidder)
    print(f"The winner is {highest_bidder} with a bid of ${value}" )



  
print("Welcome to the secret auction program ")
bids = {}
auction()

  
  

