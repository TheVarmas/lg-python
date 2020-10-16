import random

def guess_no_clues_rude():
  frm = int(input("You want to guess from ? "))
  to = int(input("to ? "))
  rn = random.randint(frm, to)
  #print(rn)

  attempts = 0
  guess = int(input(f"Guess what I'm thinking ({frm} to {to})? "))

  while (True):
    attempts += 1
    if not (frm <= guess <= to):
      message = f"You need to choose between {frm} and {to} dummy! "
    else:
      message = "Try again: "

    if guess == rn:
      print(f"Yay! You got it in {attempts} attempt(s)")
      break
    else:
      guess = int(input(message))
