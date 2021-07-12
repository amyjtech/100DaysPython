# Automate the Boring Stuff with Python
# Chapter 7 - Identifying Patterns with Regular Expressions


# Using Regular Expressions

# Importing the regex model
import re

# Creating regex object
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# Pass str you want to search using .search() method
mo = phoneNumRegex.search('My number is 415-555-4242')

print(f'Phone number found: ',mo.group())



# Matching Multiple Groups with Pipe
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')

bruce = batRegex.search('Batmobile lost a wheel')

# Returns the entire word matched
print(bruce.group())

# Returns the word within the grouping
print(bruce.group(1))


# Optional Matching with Question Mark



# Not Using Regular Expressions

# def isPhoneNumber(text):
#     if len(text) != 12:
#         return False
#     for i in range (0,3):
#         if not text[i].isdecimal():
#             return False
#         if text[3] != '-':
#             return False
#     for i in range(4,7):
#         if not text[i].isdecimal():
#             return False
#     if text[7] != '-':
#         return False
#     for i in range(8,12):
#         if not text[i].isdecimal():
#             return False
#     return True

# print('Is 415-555-4242 a phone number?')
# print(isPhoneNumber('415-555-4242'))