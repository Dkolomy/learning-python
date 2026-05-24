# Python code​​​​​​‌‌‌‌‌​‌‌​​​​​‌‌‌​‌​‌‌‌​‌​ below
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    if not type(hexNum) == str or len(hexNum) == 0:
        return None
    value = 0
    hexNum = hexNum.upper()
    for c in hexNum:
        if c not in hexNumbers:
            return None
        value = value * 16 + hexNumbers[c]
    return value
    

print(hexToDec('A'))
print(hexToDec('B'))
print(hexToDec('C'))
print(hexToDec('D'))
print(hexToDec('E'))
print(hexToDec('F'))
print(hexToDec('10'))
print(hexToDec('11'))
print(hexToDec('12'))
print(hexToDec('13'))
