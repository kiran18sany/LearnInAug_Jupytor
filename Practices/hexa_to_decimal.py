# Python code​​​​​​‌‌​‌‌‌‌​‌‌​‌‌​‌​‌​​‌​‌​​‌ below
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    is_valid = all(char.upper() in hexNumbers for char in hexNum)

    if is_valid:
        hexNum = hexNum.upper()  # ensure all letters are uppercase
        decimal_value = 0

        for i, digit in enumerate(reversed(hexNum)):
            if digit in hexNumbers:
                value = hexNumbers[digit]
                decimal_value += value * (16 ** i)
            else:
                raise ValueError(f"Invalid hex digit: {digit}")

        return decimal_value
    else:
        None

print (hexToDec('A2') )

print (hexToDec('spam') )

def hexToDec1(hexNum):
    for char in hexNum:
        if char not in hexNumbers:
            return None
    converted=0
    exponent=len(hexNum)-1
    for char in hexNum:
        converted=converted +  (hexNumbers[char]* (16 ** exponent))
        exponent-=1
    return converted

print (hexToDec1('A2') )

print (hexToDec1('spam') )

def hexToDec2(hexNum):
    for char in hexNum:
        if char not in hexNumbers:
            return None
    if len(hexNum)==3:
        return hexNumbers[hexNum[0]] *256 + hexNumbers[hexNum[1]] *16 + hexNumbers[hexNum[2]]
    if len(hexNum) == 2:
        return  hexNumbers[hexNum[0]] * 16 + hexNumbers[hexNum[1]]
    if len(hexNum) == 1:
        return hexNumbers[hexNum[0]]

print (hexToDec2('A2') )

print (hexToDec2('spam') )


print (bool(-1) )
if bool(-1) == 1:
    print('Praise God')
else:
    print('Still Praise God')