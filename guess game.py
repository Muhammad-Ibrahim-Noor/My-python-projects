import random

def difficulty(user_choice):
  
  if user_choice=='hard':
    return hard_level_turns    
  elif  user_choice=='easy':
    return easy_level_turns   
  else:
    print("Select a valid input")

def compare(guess,com_choice,turns):
  if guess>com_choice:
    return turns -1  
    print("Too high") 
      
  elif guess<com_choice:
    return turns -1  
    print("Too low.")
     
  else:
    print("You guessed it right. You got it.")


com_choice=random.randint(0,101)
print(f" psst the number is {com_choice}")   
user_choice=(input("Do you want easy or hard challenge?\n")).lower()
hard_level_turns=5
easy_level_turns=10


def game():
  guess=0 
  turns = difficulty(user_choice) 
  while guess != com_choice:
    print(f"You have {turns} turns left")
    guess=int(input("Guess a number between 1 and 100.\n"))
    turns = compare(guess,com_choice,turns)
    if turns==0:
      print("You lost. You're out of turns.")
      return
    elif guess != com_choice:
      print("GUess again nalaik")

game()