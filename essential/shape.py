# Python code​​​​​​‌‌‌‌‌​‌‌​‌​​​‌​‌‌​​​​‌​‌‌ below
class Shape:
	width = 5
	height = 5
	printChar = '#'

	def printRow(self, i):
		raise NotImplementedError("Will be implemented by children extending this class")

	def print(self):
		for i in range(self.height):
			self.printRow(i)


class Square(Shape):
	def printRow(self, i):
		print(self.printChar * self.width)

class Triangle(Shape):
	def printRow(self, i):
    # Row 0 prints 1 char, Row 1 prints 2 chars, etc.
    print(self.printChar * (i + 1))