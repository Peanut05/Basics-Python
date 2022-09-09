''' Write a programe to create a ditionary of hindi words
with values of their hindi translation. provide a user an
option to look it up !'''

dicti = {
        "bijali": "electricity",
        "rasta": "way or road",
        "ghadi": "watch",
        "diwar": "wall"
     }

print("Options are : ",dicti.keys())
a = input("Enter word for english translation : ")
print("Translation is : ",dicti[a])
print("Translation is : ",dicti.get(a)) #key is not present it tell none only
