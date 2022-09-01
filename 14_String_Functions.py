# string functions :-
'''string function are ues to perform oprations on strings'''

# 1) len():---->
# That function are use for calculate the length of the strings

story = '''Krushna wanna be a professional hacker but 
He is lezy ultra pro max'''
b = len(story)
print(b)

# 2) string.endswith() :------>
'''That functio is tells where the veriable strins endas with 
that you enterd word or not'''
# It return boolean value

c = story.endswith('ddkffl')
d = story.endswith('max')
print(c)
print(d)

# 3) string.count() :----->
# It counts a single word or charecter repeat how much time in a string

e = story.count('f')
f = story.count('l')
g = story.count('z')
h = story.count('a')

print(e)
print(f)
print(g)
print(h)

# 4) string.capitalize() ------>
''' That functions capialize the first charecter of the given strings '''
i = story.capitalize()
print(i)

# 5) string.find(word):---->
'''This function find a word and returns the index of first
occurance of that word in a string '''

print(story.find('k'))

# 7) string.replace(old_word , new_word)
''''It functions replace a old word with new word into entire string '''
print(story.replace('hacker' , 'jocker')) 
