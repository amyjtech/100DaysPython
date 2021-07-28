# Automate the Boring Stuff with Python
# Chapter 7 - Identifying Patterns with Regular Expressions

# Importing the regex model
import re

# Creating regex object
phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

# Pass str you want to search using .search() method
mo = phoneNumRegex.search("My number is 415-555-4242")

print(f"Phone number found: ", mo.group())


print("\n")
# Matching Multiple Groups with Pipe
batRegex = re.compile(r"Bat(man|mobile|copter|bat)")

bruce = batRegex.search("Batmobile lost a wheel")

# Returns the entire word matched
print(bruce.group())

# Returns the word within the grouping
print(bruce.group(1))


print("\n")
# Optional Matching with Question Mark
batRegex = re.compile(r"Bat(wo)?man")

mo1 = batRegex.search("The Adventures of Batman")
print(mo1.group())

mo2 = batRegex.search("The Adventures of Batwoman")
print(mo2.group())


print("\n")
# Matching Specific Repetiions w/ Braces

# This will match any str that has 'Ha' 3 or more times
haRegex = re.compile(r"(Ha){3}")

# Matches
mo1 = haRegex.search("HaHaHa")
print(mo1.group())

# Does not match
mo2 = haRegex.search("Ha")
print(mo2 == None)

# Matches
mo3 = haRegex.search("HaHaHaHaHa")
print(mo3.group())


print("\n")
# FindAll() Method

# search() returns the first matched text in the searched str
phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

mo = phoneNumRegex.search("Cell: 415-555-9999 Work: 212-555-0000")
print(f"search() method", mo.group())

# findall() returns EVERY match in the searched str
phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

mo2 = phoneNumRegex.findall("Cell: 415-555-9999 Work: 212-555-0000")
print(f"findall() method", mo2)


print("\n")
# Making your own Character Class

# Use [ ] to create custom character classes
# This character class will match any vowel lowercase or uppercase
vowelRegex = re.compile(r"[aeiouAEIOU]")

mo = vowelRegex.findall("RoboCop eats baby food. BABY FOOD.")
print(mo)

# Create a negative custom character class
# This will match all characters NOT in the character class
consonantRegex = re.compile(r"[^aeiouAEIOU]")

mo2 = consonantRegex.findall("RoboCop eats baby food. BABY FOOD.")
print(mo2)


print("\n")
# Using the Caret Character

# The caret symbol indicates a match at the beginning
startHello = re.compile(r"^Hello")

mo = startHello.search("Hello, world!")
print(mo)

mo2 = startHello.search("He said hello")
print(mo2 == None)


print("\n")
# Using the Dollar Sign Character

# The dollar sign symbol indicates a match at the end
endNum = re.compile(r"\d$")

mo = endNum.search("Your number is 42")
print(mo)

mo2 = endNum.search("Your number is forty-two")
print(mo2 == None)


# Example of searching a phone number NOT using regular expressions

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
