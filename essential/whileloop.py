from datetime import datetime

# While loop
print(datetime.now().second)

# wait_until = (datetime.now().second + 5) % 60
# while datetime.now().second != wait_until:
#   print('Waiting for the next second...')
# print('Done')

print('======================')

# Pass
# wait_until = (datetime.now().second + 2) % 60
# while datetime.now().second != wait_until:
#   print(datetime.now().second)
#   pass
# print('Done')

# print('======================')

# Break
# wait_until = (datetime.now().second + 5) % 60
# while True:
#   if datetime.now().second == wait_until:
#     print(f'We are at {wait_until} seconds!')
#     break
# print('Done')

# print('======================')

# Continue
wait_until = (datetime.now().second + 2) % 60
while True:
  if datetime.now().second < wait_until:
    continue
  break
print('Done')
