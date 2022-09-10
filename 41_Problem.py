''' Create an empty ditionary allow 5 friends to enter their
favourite fruit as a values use keys as their names assume
that the name are unique '''

favfruit = {} #empty dictionary

a = input("Enter your favourite fruit Soham :\n")
b = input("Enter your favourite fruit Rohit :\n")
c = input("Enter your favourite fruit Prasad :\n")
d = input("Enter your favourite fruit shubham :\n")
e = input("Enter your favourite fruit ravi :\n")

favfruit['soham'] = a
favfruit['rohit'] = b
favfruit['prasad'] = c
favfruit['shubham'] = d
favfruit['ravi'] = e

print(favfruit)

''' If you entered same favourite fruit of 
two friends then what will happen 
-----------------=========>>>>>>>>>>>
[nouthing will happens 
there are need to use difffetent keys not value] '''
