import random

def guess_with_clues():
  frm = int(input("You want to guess from ? "))
  to = int(input("to ? "))
  rn = random.randint(frm, to)
  #print(rn)

  attempts = 0
  guess = int(input(f"Guess what I'm thinking ({frm} to {to})? "))

  while (True):
    attempts += 1
    if guess > rn:
      message = "Go lower! "
    elif guess < rn:
      message = "Go higher!  "
    
    if guess == rn:
      print(f"Yay! You got it in {attempts} attempt(s)")
      break
    else:
      guess = int(input(message))
