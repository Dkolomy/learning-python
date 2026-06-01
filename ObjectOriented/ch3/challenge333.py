# Python code​​​​​​‌‌‌‌‌​‌‌​‌‌‌‌​​‌​‌‌‌‌‌‌‌​ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

class Stock:
    def __init__(self, ticker, price, company):
        self.ticker = ticker
        self.price = price
        self.company = company

    # Put your comparison logic here.
    def __eq__(self, other):
        if not isinstance(other, Stock):
            return ValueError("Cannot compare Stock with non-Stock object")
        return self.ticker == other.ticker and self.price == other.price and self.company == other.company

    def __lt__(self, other):
        if not isinstance(other, Stock):\
            return ValueError("Cannot compare Stock with non-Stock object")
        return self.price < other.price

    def __gt__(self, other):
        if not isinstance(other, Stock):
            return ValueError("Cannot compare Stock with non-Stock object")
        return self.price > other.price

    def __ge__(self, other):
        if not isinstance(other, Stock):
            return ValueError("Cannot compare Stock with non-Stock object")
        return self.price >= other.price

    def __le__(self, other):
        if not isinstance(other, Stock):
            return ValueError("Cannot compare Stock with non-Stock object")
        return self.price <= other.price
