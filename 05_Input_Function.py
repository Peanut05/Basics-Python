# Input Functio :-
''' That function allows to the users to take input from the keyboard as a strin
until you convert into int,float or any other data types using typecasting 
a = input("Enter your Name")  it's get that user entered into it'''

a = input("Enter your name ")
print(a,type(a))
b = input("Enter a digit ")
b = int(b) # convert a to integer
print(b,type(b))
print(b+10)
