import random
from art import logo
from art import vs
from game_data import data
from replit import clear



def format_data(account):
  """"format the data into printable format """
  account_name = account['name']
  account_description = account['description'] 
  account_country = account['country']
  return (f"{account_name}, a {account_description}, from {account_country}.")
  


def check_answer(guess,follower_count_1,follower_count_2 ):
  """"Take the guess, follower counts and return if they got it right """
  if guess == "a":
    if follower_count_1 > follower_count_2 :
      return True
    else:
      return False
  else:
    if follower_count_2 > follower_count_1:
      return True
    else:
      return False
    
    
  
# Display art 

print(logo)
score = 0
game_continue = True
account2 = random.choice(data)
#Make game repeatable 
while game_continue:
  #generate a random account from the game data
  account1 = account2
  account2 = random.choice(data)
  if account1 == account2:
    account2 = random.choice(data)
  
  print(f"compare A: {format_data(account1)}")
  
  print(vs)
  
  print(f"Compare B: {format_data(account2)}")
  
  #ask the user for a guess
  
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  # check if user is correct
  #check how many follower each have
  
  follower_count_1 = account1["follower_count"]
  follower_count_2 = account2["follower_count"]
  
  
  #give user a feedback
  #tracking score
  is_correct = check_answer(guess,follower_count_1,follower_count_2)
  clear()
  if is_correct == True:
    score +=1
    print(f"Yes, you are right! current score = {score}")
  else:
    game_continue = False
    print(f"You are wrong! finale score = {score}")

#making the account at position B become the next account at position A
    