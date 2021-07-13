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


print('\n')
# Matching Multiple Groups with Pipe
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')

bruce = batRegex.search('Batmobile lost a wheel')

# Returns the entire word matched
print(bruce.group())

# Returns the word within the grouping
print(bruce.group(1))


print('\n')
# Optional Matching with Question Mark
batRegex = re.compile(r'Bat(wo)?man')

mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())


print('\n')
# Matching Specific Repetitions w/ Braces
haRegex = re.compile(r'(Ha){3}')

# Matches regex
mo1 = haRegex.search('HaHaHa')
print(mo1.group())

# Does not match regex since there is iteration
mo2 = haRegex.search('Ha')
print(mo2 == None)

# (Ha){3} matches 3 or more of the same
mo3 = haRegex.search('HaHaHaHa')
print(mo3.group())


print('\n')
# FindAll() Method

# search() returns the first matched text in the searched str
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(f'search() method\n',mo.group())

# findall() returns EVERY match in the searched str
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo2 = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(f'findall() method\n',mo2)




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