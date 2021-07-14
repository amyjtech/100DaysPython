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
    )''',re.re.VERBOSE)

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

# 4. Join matches into str for clipboard