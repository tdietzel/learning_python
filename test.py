print("----------Functions & if-else loops-----------")
# ------------------------------------------------------------------------

test = 4.55 # float

if test > 5:
  print("Bigger than 5")
elif test < 5:
  print("Less than 5") #triggers
else:
  print("error")

def newValue(test):
  test += 1
  print("The new value: ", test) #triggers as 5.55
  return test

def checkValue(test):
  if test > 5:
    print("Greater than 5") #triggers
  elif test < 5:
    print("Less than 5")
  else:
    print("Equal to 5")

test = newValue(test)
checkValue(test)

print("********************") # --------------------------

findMax = max('Test') # lowercase takes precedence
print(findMax) # returns t


print("----------Loops-----------")
# ------------------------------------------------------------------------
# can use 'break' & 'continue' in loops

x = 10
while x <= 10 and x > 0: #operator 'and'
  if x == 3: # double == to compare
    print("Ground shakes")
  print("...", x)
  x = x - 1
print("Blastoff!")

print("********************") # --------------------------

for time in [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]:
  if time == 3:
    print("Ground shakes")
  print('...', time)
print("Blastoff!")

print("------- LARGEST NUMBER IN ARRAY --------") # ------- LARGEST NUMBER IN ARRAY --------

arr = [5, 6, 2, 1, 12, 9, 25, 3] #replace with any #'s
def largestNum(arr):
  largest_num = -1
  for num in arr:
    if largest_num < num:
      largest_num = num
  print(largest_num) #print '25'
largestNum(arr)

print("------- STRING LENGTH --------") # ------- STRING LENGTH --------

string = 'How long?' #replace with any string
def stringLength(string):
  length = len(string)
  return length
print('String Length:', stringLength(string)) #print 9

print("********************") # --------------------------

string = "Python Slice"
print(string[:6]) #not-including i(6)
print(string[7:]) #including i(7)
print(string[2 : 6]) #including i(2) but not i(6)

#built in functions to string
print(string.upper())
print(string.lower())
print(string.replace('Slice', 'Replace'))
print(string.startswith("Python")) #returns true
print(string.find('Slice')) #returns 7 the i(S)

print("------- WORD FINDER --------") # ------- WORD FINDER --------
# REMOVE comments below to enter in your own passage through the terminal!
  # text = input("Enter a passage:").lower()
  # searchWord = input("Enter word to search for:").lower()

text = 'The quick brown fox jumps over the lazy dog.'
searchWord = 'lazy'
def wordFinder(text, searchWord):
  if searchWord in text:
    print(searchWord, 'was found') #triggers
  else:
    print(searchWord, 'was not found')
wordFinder(text, searchWord)

print("------- DICTIONARY --------") # ------- DICTIONARY --------

sportTeams = { 'OSU': "Oregon State University", 'UO': "University of Oregon"}
print(sportTeams['OSU'])

print("------- Word Occurrences --------") # ------- Word Occurrences --------

text = "The apple orchard is full of ripe apples, and I love to eat a juicy apple every day."

def wordOccurrence(text):
  words = text.split(' ')
  count = {}
  for word in words:
    if word in count:
      count[word] += 1
    else:
      count[word] = 1
  highest_word = max(count, key = count.get)
  word_occurrences = count[highest_word]
  print("Most common word: ", highest_word)
  print("Number of occurrences: ", word_occurrences)
wordOccurrence(text)

# PYTHON SYNTAX   | EXAMPLE / EXPLANATION
# ---------------------------------------------
# \n              | new line
# len             | length
# in              |
# not in          | 
# upper()         | toUpper()
# lower()         | toLower()
# replace('', '') | replaces part of a string
# startswith()    | returns T or F
# def             | defines a function
# elif            | else if
# and             | &&
# print()         | console.log()
# open()          | open a specific file
# strip()         | 
# rstrip()        | 
# quit()          | terminate program
# range(x)        | returns list of #'s that range from 0 to x - 1
# List Methods    | x = list()
# ...               dir(x) - returns built in list methods
# ...               type(x) - returns type
# ...               append() - add elements to a list
# ...               len(x) - returns list length
# ...               max(x) - returns biggest num in list
# ...               min(x) - returns smallest num in list
# ...               sum(x) - returns sum of all numbers in list
# ...               sort(x) - changes order of list to be sorted
# split(x)        | removes spaces in a string and returns a list of strings or words
# dict            | dictionary
# ...               get(key, value) - default: value = 0