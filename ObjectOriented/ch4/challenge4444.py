# Python code​​​​​​‌‌‌‌‌​‌‌​‌‌‌‌​‌​​‌‌‌​​​‌​ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

class Asset():
    def __init__(self, price):
        self.price = price


class Stock(Asset):
    def __init__(self, price, ticker, company):
        super().__init__(price)
        self.ticker = ticker
        self.company = company


class Bond(Asset):
    def __init__(self, price, description, duration, interest):
        super().__init__(price)
        self.description = description
        self.duration = duration
        self.interest = interest
