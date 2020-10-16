from Games.GuessingGameNoClues import guess_no_clues
from Games.GuessingGameNoCluesRude import guess_no_clues_rude
from Games.GuessingGameWithClues import guess_with_clues
from Games.GuessingGameWithCluesRude import guess_with_clues_rude
from Games.Tables import mult_tables
from Utils.ostools import clear

valid_options = ['a', 'b', 'c', 'd', 'e', 'f']
invalid_option_msg = "Invalid option!"
bye_msg = "Hope you had fun. Bye!"
options = """Which game do you want to play?
\t a) Guessing game with no clues
\t b) Guessing game with no clues rude version
\t c) Guessing game with clues
\t d) Guessing game with clues rude version
\t e) Print mutiplication tables
\t f) No more games. Just let me out!
\n"""

choice_prompt = f"Choose an option from '{valid_options[0]}' to '{valid_options[-1]}' and press enter: "

#chosen_option = str(input(options + choice_prompt)).lower()

while True:
  chosen_option = str(input(options + choice_prompt)).lower()
  print("\n")

  if chosen_option not in valid_options:
    chosen_option = str(input(invalid_option_msg + " " + choice_prompt)).lower()
  else:
    if chosen_option == 'a':
      guess_no_clues()      
    elif chosen_option == 'b':
      guess_no_clues_rude()
    elif chosen_option == 'c':
      guess_with_clues()
    elif chosen_option == 'd':
      guess_with_clues_rude()
    elif chosen_option == 'e':
      mult_tables()
    else:
      print(bye_msg)
      break

    input("\nPress any key to continue...")
    clear()

  


