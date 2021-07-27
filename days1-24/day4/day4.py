# Automate the Boring Stuff with Python
# Chapter 8 - Input Validation

import pyinputplus as pyip


#response = pyip.inputNum()
# Requires a int for input, str or other data types will not work

# /// min, greaterThan, lessThan

#response = pyip.inputNum('Enter a number: ', min=4)

#response1 = pyip.inputNum('Enter a number:', greaterThan=5)

#response2 = pyip.inputNum('>: ', min=2, lessThan=6)

# /// blank keyword arg

#response = pyip.inputNum('Enter a num: ')

# blank makes input optional so the user does not have to enter anything
#blank = pyip.inputNum('Enter a num: ', blank=True)

# /// limit, timeout, default keyword args

# Gives x amount of tries to enter correct input
#limit = pyip.inputNum(limit=2)

# Gives x amount of seconds to press enter after typing input
#timeout = pyip.inputNum(timeout=10)

# Returns a blank value or a str as the value if max tries reached
#response = pyip.inputNum(limit=2, default='N/A')

# /// Using Custom Validation

def addUpTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('The digits must add up to 10, not %s' %
                        (sum(numbersList)))
    return int(numbers)


#response = pyip.inputCustom(addUpTen)
