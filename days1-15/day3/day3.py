# Automate the Boring Stuff with Python
# Phone Number and Email Address Extractor w/ pyperclip

import pyperclip, re

# 1. Create a Regex for phone numbers
phoneRegex = re.compile(r'''(
    # Area Code -- ? means it is optional
    (\d{3}|\(\d{3}\))?
    # - or . seperator
    (\s|-|\.)?
    # 3 digits
    (\d{3})
    # - or . seperator
    (\s|-|\.)
    # 4 digits
    (\d{4})
    # ext, x, or ext. for extension
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''',re.VERBOSE)

# 2. Create a Regex for email addresses
emailRegex = re.compile(r'''(
    # Username
    [a-zA-z0-9._%+-]+
    # @ symbol
    @
    # Domain name
    [a-zA-z0-9.-]+
    # .com, .org, .edu, etc
    (\.[a-zA-Z{2,4}])
)''',re.VERBOSE)

# This will expression will catch most emails, but will not match EVERY possible email.

# 3. Find all matches in clipboard text
txt = str(pyperclip.paste())

matches = []

for groups in phoneRegex.findall(txt):
    # Searching Phone #
    # Contains str from groups 1, 3 & 5 -- area code, 3 digits, 4 digits
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    # Checking for group 8 and appending if found -- extension
    if groups[8]!= '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

    # Searching Emails
    # Appending the entire expression [0]
    for groups in emailRegex.findall(txt):
        matches.append(groups[0])

# 4. Join matches into str for clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

# Copied text from nostarch.com/contactus/