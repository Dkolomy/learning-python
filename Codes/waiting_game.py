# Your goal is to implement a function, waiting_game(), that prints a message for the player to wait 
# a random amount of time, somewhere between two to four seconds. When the player presses 
# Enter, that starts a timer. The player's goal is to wait the specified number of seconds and then 
# press Enter again. That displays the elapsed time, along with a message about whether the player 
# was too fast, too slow, or right on target.

import time
import random

def waiting_game():
  target_time = random.randint(2, 4)
  print(f"You have {target_time} seconds to press the enter key.")

  input("Press Enter to start")
  start_time = time.time()

  input("Press Enter to stop")
  end_time = time.time()

  elapsed_time = end_time - start_time
  print(f"Elapsed time: {elapsed_time} seconds")

  if elapsed_time == target_time:
    print("Perfect!")
  elif elapsed_time < target_time:
    print(f"You were {target_time - elapsed_time} seconds too fast!")
  else:
    print(f"You were {elapsed_time - target_time} seconds too slow!")

waiting_game()