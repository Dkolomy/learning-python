# slice a string
my_string = "Hello, World!"
print(my_string[0:5])
print(my_string[7:12])
print(my_string[7:])
print(my_string[:5])
print(my_string[-5:])
print(my_string[-5:-2])
print(my_string[-5:-2:2])

myList = [1, 2, 3, 4, 5]
print(myList[0:5])
print(myList[7:12])
print(myList[7:])
print(myList[:5])
print(myList[-5:])
print(myList[-5:-2])
print(myList[-5:-2:2])

# Format a string
name = "John"
age = 30
city = "New York"
print(f"My name is {name} and I am {age} years old and I live in {city}")
print("My name is {0} and I am {1} years old and I live in {2}".format(name, age, city))
print("My name is {name} and I am {age} years old and I live in {city}".format(name=name, age=age, city=city))
print("My name is {0} and I am {1} years old and I live in {2}".format(name, age, city))
print("My name is {0} and I am {1} years old and I live in {2}".format(name, age, city))

# Multi-line strings
my_string = """This is a multi-line string.
asdsadasdasd
gggggggggggggg """
print(my_string)