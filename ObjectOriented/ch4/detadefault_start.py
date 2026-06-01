# Python Object Oriented Programming by Joe Marini course example
# implementing default values in data classes

from dataclasses import dataclass, field
import random

def price_func():
    return float(random.randrange(20, 50))

@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str = "No title"
    author: str = "No author"
    pages: int = 0
    price: float = field(default_factory=price_func)

# b1 = Book()
# print(b1)

b2 = Book("To Kill a Mockingbird", "Harper Lee", 209)
b3 = Book('The Great Gatsby', 'F. Scott Fitzgerald', 180)

print(b2)
print(b3)