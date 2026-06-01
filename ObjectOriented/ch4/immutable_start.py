# Python Object Oriented Programming by Joe Marini course example
# Creating immutable data classes

from dataclasses import dataclass


@dataclass(frozen=True)  # TODO: "The "frozen" parameter makes the class immutable
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0


obj = ImmutableClass()
print(obj.value1, obj.value2)

# TODO: attempting to change the value of an immutable class throws an exception
# obj.value1 = "New Value"
# print(obj.value1, obj.value2)

# TODO: even functions within the class can't change anything
# def change_it(self):
#     self.value1 = "New Value"

# change_it(obj)
# print(obj.value1, obj.value2)