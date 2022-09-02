'''Write a programe to fill in a letter template given bilow 
as name and date 
dear,<name>
you are selected!
Date : <date>'''

name = input("Enter the name :")
date = input("Enter date :")
print("Dear," + name)
print("You are selected!")
print("Date :",date)

# Using string function :--->

letter = '''Dear,<name>
you are selected!
for the job in our company
Date :<date>'''

name1 = input("Enter your name for 2nd letter : ")
date1 = input("Enter your name for 2nd letter : ")
letter = letter.replace("<name>" , name1)
letter = letter.replace("<date>" , date1)
print(letter)
