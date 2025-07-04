# CoffeeCodeBox - Mohammadreza Sa.
import re

# initialization
text = ""
regex = None

# the first arg is the text you wanna check. the second will be your regular expression
def setup(txt, rgx):
    global text, regex
    text, regex = txt, rgx

# returning if the text matches your pattern will be done using the SEARCH() METHOD in Python
def test():
    print(f"the result of {regex} with the text of \"{text}\" is {bool(re.search(regex, text))}")

# returning the values matching your pattern will be done using the FINDALL() METHOD in Python
def match():
    print(f"the regex {regex} for the text \"{text}\" has these occurrences: {re.findall(regex, text)}")

# replacing will be done using the SUB() METHOD in Python
# suppose text has to be changed → the substrings matching regex will be replaced by txt
def replace(txt):
    global text
    text = re.sub(regex, txt, text)

# single word lookup
setup("hello man", r"hello")
test()  # true -> one word matches the pattern

# various options (like the OR bitwise operator)
setup("I've got two dogs.", r"cat|dog|bird|fish")
test()  # true -> the "dog" will be found in the text

# ///////// NOTE: REGEX IS CASE SENSITIVE /////////

# example
setup("I'VE GOT TWO DOGS", r"cat|dog|bird|fish")
test()  # false -> being case-sensitive, none of the words matches the pattern

# In Python, regex flags like "i" and "g" are added via re.IGNORECASE, re.MULTILINE, etc., when compiling the regex

# telling it to be case insensitive, using "i" flag
setup("I'VE GOT TWO DOGS", re.compile(r"cat|dog|bird|fish", re.I))
test()  # true -> being case-insensitive, the "DOG" word matches the pattern

# extracting the first matching occurrence in the text
setup("Twinkle, twinkle, little star...", re.compile(r"twinkle", re.I))
match()  # ["Twinkle"] -> being case-insensitive, returns the "Twinkle" as the first match

# using re.IGNORECASE for case-insensitive and re.findall() for global (all matches)

# extracting all matching occurrences in the text, using "g" flag
setup("Twinkle, twinkle, little star...", re.compile(r"twinkle", re.I))
match()  # ["Twinkle", "twinkle"] -> returns all occurrences

# finding words with wildcard characters -> e.g. /.un/ => run, pun, sun, gun etc.
setup("it should be fun to learn regular expressions during the sunset", r".un")
match()  # ["fun", "sun"] -> returns all occurrences

# determining specific characters for the search, using []
setup("oh, boy! i see big bugs!", re.compile(r".[auoie].", re.I))
match()  # ["boy", " i ", "see", "big", "bug"] -> returns all occurrences (vowels in this example)

# determining a range of characters for the search, using DASH
setup("oh, boy! i see big bugs!", re.compile(r"[a-z]", re.I))
match()  # -> returns all of the letters in the text

# including a combination of letters and numbers (b to f + 1 to 6)
setup("I've been there 4 the 2nd time", re.compile(r"[b-f1-6]", re.I))
match()  # [e,b,e,e,e,e,4,e,2,d,e] -> returns all occurrences

# EXCLUDING A SET OF CHARACTERS FROM THE MATCH PICKUP

# typically, you may wanna use ^ char to exclude a specified charset
setup("I was born in 2008", r"[^0-9]")
match()  # -> returns all of the non-numeric characters in the text

# SEARCHING FOR A *** ONCE-OR-MORE-TIMES-REPEATED *** CHARACTER

# gotta use + sign right after the desired character
setup("Mississippi", re.compile(r"s+", re.I))
match()  # ["ss", "ss"]
# adding an extra s to the end of the word
setup(f"{text}s", re.compile(r"s+", re.I))
match()  # ["ss", "ss", "s"]

# SEARCHING FOR A *** ZERO-OR-MORE-TIMES-REPEATED *** CHARACTER (OPTIONAL ACTUALLY)

# gotta use * sign right after the desired character
# in this example, any expression starting with G (case sensitive) and then followed up by (o)s, which is completely optional due to the * sign, will be extracted
# THE * SIGN POINTS ONLY AT THE CHARACTER BEHIND, WHICH IS "o" HERE
setup("Google", r"Go*")
match()  # ["Goo"]
# adding i flag to the regex
setup("Google", re.compile(r"Go*", re.I))
match()  # ["Goo", "g"] -> being insensitive to the case, it includes every "g"

# THERE ARE TWO TYPES OF EXTRACTING MATCHING EXPRESSIONS IN REGEX
# 1.GREEDY 2.LAZY
# GREEDY MATCH PICKS UP THE LONGEST MATCH IN THE TEXT
# LAZY MATCH, ON THE OTHER HAND, PICKS UP THE SHORTEST MATCH IN THE TEXT
# IMPORTANT: regex uses greedy match by default
# greedy match example
setup("<p>hello</p>", r"<.*>")
match()  # ["<p>hello</p>"]
# using a question mark just before the last character to switch to LAZY MATCH
setup("<p>hello</p>", r"<.*?>")
match()  # ["<p>"]
# picking all of the matching parts
setup("<p>hello</p>", r"<.*?>")
match()  # ["<p>", "</p>"]

# checking if the text starts with the desired expression
setup("Alexa's been weak", re.compile(r"^alexa", re.I))
test()  # true -> starts with "alexa" (case-insensitive)

# checking if the text ends with the desired expression
setup("Alexa's been weak", re.compile(r"weak$", re.I))
test()  # true -> ends with "weak"

# picking lowercase and uppercase chars, numbers and underscores of a text
# using SHORTHAND CHARACTERSET CLASS (\w)
setup("Hello my world!", r"\w")
match()  # returns all of the letters, excluding spaces and the exclamation mark
# getting the length of characters
print(len(re.findall(regex, text)))  # 12

# doing the opposite: picking anything except the characters mentioned in the previous example
# using \W class
setup("Hello my world!", r"\W")
match()  # returns spaces and the exclamation -> [" ", " ", "!"]
# getting the length of characters
print(len(re.findall(regex, text)))  # 3

# accessing the numbers in a text
# using \d class
setup("your order will be 12.99$", r"\d")
match()  # returns all digits -> ["1", "2", "9", "9"]

# accessing all non-numeric characters
# using \D class
setup(text, r"\D")
match()  # returns all letters and non-numeric characters

# EXERCISE: VALIDATE USERNAMES WITH 3 CONDITIONS:
# 1. letters come first and then numbers(which are optional)
# 2. letters could be uppercase or lowercase
# 3. minimum length of the letters should be 2
# The answer:
setup("CoffeeCodeBox23", re.compile(r"^[a-z]{2,}\d*$", re.I))
# the {} determines the length of required matches for the expression behind it
# in this example, the minimum is 2 and the maximum is undefined
test()  # true

# accessing the whitespaces(spaces, newlines, tabs, etc.)
# using \s class
setup("your order will be 12.99$", r"\s")
match()  # returns all of the spaces (4 spaces)

# HOW TO WORK WITH QUANTITY SPECIFIERS
# YOU COULD SPECIFY HOW MANY TIMES A SINGLE CHARACTER OF A CHARACTERSET SHOULD MATCH A PATTERN
# in these examples, we determine how many time should "l" be repeated
# 1. using a definite value
setup("hellllo!", r"^hel{2}o!")
test()  # false -> 2 != 4
# 2. using a range -> the first value is the min and second one is the max (optional)
setup("hellllo!", r"^hel{2,4}o!")
test()  # true -> 2 < 4 <= 4

# EXERCISE: validate emails using regex
# THE ANSWER:
setup("myemail@host.com".lower(), re.compile(r"^[a-z]{1,}[a-z0-9_]{2,}@[a-z]{2,15}[.]{1}[a-z]{2,8}$"))
test()  # true -> it's valid

# checking the possible existence of a character with a ?
setup("favourite", r"favou?rite")
test()  # true, even if you remove the letter "u"

# LOOKAHEADS = YOU CAN CHECK THE STATE OF BEING OR NOT BEING OF A CHARACTER AFTER ANOTHER CHARACTER
# THERE ARE TWO TYPES OF LOOKAHEAD -> 1.positive  2.negative
# positive -> using (?=x)
setup("quit", r"q(?=ui)")
match()  # ["q"] -> first checks for "q" and then checks if a "ui" exists right after it
# negative -> using (?!x)
setup("quest", r"q(?!ui)")
match()  # ["q"] -> first checks for "q" and then checks if there's no "ui" after it

# CAPTURE GROUPS: A SHORTHAND OF DEFINING CHARSETS OR CHARACTERS
# THEY ARE LIKE A PLACEHOLDER FROM WHICH YOU COULD ABSOLUTELY USE AS MANY TIMES AS YOU NEED
# example
setup("AI AI", re.compile(r"(\w+)\s\1", re.I))
match()  # ["AI AI"]
# example
setup("10 20 10 20", re.compile(r"(\d+)\s(\d+)\s\1\s\2"))
match()  # ["10 20 10 20"]
# YOU MIGHT ALSO SEE EXTRA OPTIONS AT THE END OF THE ARRAY IF YOU DON'T USE A "g" FLAG. THOSE VALUES WOULD BE THE VALUES OF YOUR CAPTURE GROUPS.

# REPLACEMENT
# simple replacement example
setup("the silver sky", r"silver")
replace("blue")  # replaces silver with blue
print(f"REPLACED TEXT: {text}")

# replacement using capture groups
setup("world hello", re.compile(r"(\w+)\s(\w+)", re.I))
replace(r"\2 \1")  # changes the place of the capture groups
# the \2 refers to the second capture group and the \1 refers to the first one. So on...
print(f"REPLACED TEXT: {text}")

# Congrats! You can now effectively use regex — keep learning and good luck!