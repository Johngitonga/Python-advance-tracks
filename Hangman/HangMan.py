""" 
create a list of words
pick a random word from list
print a dash for each letter
prompt user to guess a letter
if letter in word, replace all occurencies in correct positions.
print previously correct guessed letters together with remaining dashes
prompt user for another guess.
if letter not in word; error message (letter not in word)
prompt user to guess again.
document wrongly guessed letters.
add stick to the figure body
keep track of guesses.

"""
import string
import random
images=["""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
"""]
list_of_words=open('words.txt', 'r')

words=list(list_of_words)

def pick_random_word(word):
	return random.choice(words)[:-1]

def replace_characters(string):
	guess=""
	dash="_"
	count=1
	imagecount=1
	for each in string:
		guess=guess+dash

	dash_list = list(guess)
	dash_string=str (dash_list)
	# print "".join(dash_string)

	while count<=len(string)+1:
		print dash_list
		i=raw_input("Type a character to see if it is in the hidden word: ") 
		if i in string:
			for index, letter in enumerate(string):
				if i == letter:
					dash_list[index]=i
		else:	
			print images[imagecount] 
		count+=1 
		if len(images)==imagecount:
			imagecount+=0
		else:
			imagecount+=1
	print "The word was: "+string

	
string=pick_random_word(words)
replace_characters(string)
 

