# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret"

    # TODO: create instance methods
    def getPrice(self):
      if hasattr(self, '_discount'):
        return self.price * (1 - self._discount)
      else:
        return self.price

    def setDiscount(self, amount):
        self._discount = amount


# TODO: create some book instances
b1 = Book("War and Peace", "Leo Tolstoy", 100, 10)
b2 = Book("The Catcher in the Rye", "J.D. Salinger", 288, 15)

# TODO: print the price of book1
print(b1.getPrice())

# TODO: try setting the discount
b1.setDiscount(0.25)
print(b1.getPrice())

# TODO: properties with double underscores are hidden by the interpreter
print(b1._Book__secret)