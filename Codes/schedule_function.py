# Your goal is to implement a function, schedule_function(), that takes three inputs arguments 
# for the time at which to run a specified function, the function you want to execute, and a 
# variable number (zero or more) of arguments which are passed to the schedule function to use.
# When your schedule_function() is called, it should immediately print a message indicating 
# which function was scheduled and when it will execute.

# This line imports the 'scheduler' class from Python's built-in 'sched' module.
# The 'scheduler' can be used to schedule functions to execute at specific times or after certain delays.
from sched import scheduler
# This line imports the 'time' module, which provides functions for working with time-related operations.
import time

def schedule_function(event_time, function, *args):
  s = scheduler(time.time, time.sleep)
  print(f"Function {function.__name__} scheduled to run at {event_time}")

  s.enterabs(event_time, 1, function, argument=args)
  s.run()

schedule_function(time.time() + 5, print, "Hello, World!")


