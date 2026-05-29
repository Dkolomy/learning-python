# with open('data.csv', 'r') as f:
#   reader = csv.reader(f, delimiter=',')
#   headers = next(reader)
#   print(headers)
#   for row in reader:
#     print(row)

# with open('data.csv', 'r') as f:
#   reader = csv.DictReader(f, delimiter=',')
#   for row in reader:
#     print(row['name'], row['age'], row['city'])    # return a dictionary

# Filtering data
# with open('data.csv', 'r') as f:
#   reader = list(csv.DictReader(f, delimiter=','))
#   print(reader)    # return a list of dictionaries
#   filtered_reader = [row for row in reader if row['age'] > 30]
#   print(filtered_reader)

# data = [row for row in data if int(row['postal_code']) is primes and row['state_code'] == 'MA']
# print(data)

with open('data.csv', 'w') as f:
  writer = csv.writer(f, delimiter=',')
  writer.writerow(['name', 'age', 'city'])
  writer.writerow(['John', 30, 'New York'])
  writer.writerow(['Jane', 25, 'Los Angeles'])
  writer.writerow(['Jim', 35, 'Chicago'])