import random

def guess_with_clues_rude():
  # Constants
  insult = ", dum dum!!"
  go_low = "Go lower"
  go_high = "Go higher"

  frm = int(input("You want to guess from ? "))
  to = int(input("to ? "))
  rn = random.randint(frm, to)
  #print(rn)

  attempts = 0
  message = ""
  prev_guess = guess = int(input(f"Guess what I'm thinking ({frm} to {to})? "))

  while (True):
    attempts += 1
    msg_insult = ""

    if (message == go_low and guess > prev_guess) or (message == go_high and guess < prev_guess):
      msg_insult = insult

    if guess > rn:
      message = go_low
    elif guess < rn:
      message = go_high
        
    if guess == rn:
      print(f"Yay! You got it in {attempts} attempt(s)")
      break
    else:
      guess = int(input(message + msg_insult + " "))
