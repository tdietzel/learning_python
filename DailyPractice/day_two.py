def warmUp(num):
  if num > 50:
    gain = num * 0.7
  elif num > 10:
    gain = num * 0.75
  elif num <= 10:
    gain = num * 80
  else:
    print("Error")
  print(gain)
num = 100
warmUp(num)

grades = {'a': 90, 'b': 80, 'c': 70, 'd': 60, 'f': 50}
students = { 'Emily': 65, 'Michael': 72, 'Sarah': 81, 'David': 90, 'Jessica': 55, 'Christopher': 78, 'Olivia': 88, 'Ethan': 93, 'Madison': 68, 'Jacob': 97}
print(sorted(students.items()))

# Regular Expressions
# ----------------------------------------------------------------
#  ^          | Matches the beginning of a line
#  $          | Matches the end of a line
#  .          | Matches any character
#  \s         | Matches whitespaces
#  \S         | Matches any non-whitespace character
#  *          | Repeats a character 0 or more times
#  *?         | Repeats a character 0 or more times (non-greedy)
#  +          | Repeats a character 1 or more times
#  +?         | Repeats a character 1 or more times (non-greedy)
#  [aeiou]    | Matches a single character in the listed set
#  [^XYZ]     | Matches a single character not in the listed set
#  [a-z0-9]   | The set of characters can include a range
#  (          | Indicates where string extraction is to start
#  )          | Indicates where string extraction is to end
# 
# import re   | Import statement for Regular Expression
# re.search() | Returns true/false depending if the string matches the regular expression
# re.findall()| Extracts the matching strings

# ^From '.*@ ([^ ] *) '
# if len(x) != -1:

# Ports
# --------------------------
# Telnet (23)        | Login
# SSH (22)           | Secure login
# HTTP (80)          |
# HTTPS (443)        | Secure
# SMTP (25)          | Mail
# IMAP (143/220/993) | Mail retrieval
# POP (109/110)      | Mail retrieval
# DNS (53)           | Domain name
# FTP (21)           | File transfer

# Project Ideas
# findall or search function practice?
# pull an email from a paragraph using find all
# make a socket
# use a socket to get back a web browser from a website or API call

# BeautifulSoup Python library is used for parsing HTML documents and extracting data from HTML documents