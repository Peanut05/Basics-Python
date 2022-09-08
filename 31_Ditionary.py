# Ditionary :--->
# Ditionary is collection of key value pairs
# Ditoinary is unordered.
# It is mutable. there can be change value in ditionary
# It is indexed
# ditionary cannot contain duplicate keys.[it overwrites]
# syntax of a ditionary :---> 

''' ditionary = {"key" : "value"
                 "One" : "1"
                 "two" : "2"
                 "six" : "6"
                 "ten" : "10"
                 "list" : [1,2,6,10]
                } 

                ditionary["key"] = prints "value"
                ditionary["one"] = prnts "one"
                ditionary["list"] = prints [1,2,6,10] '''

dict1 = {   "key": "value",
            "one": "ONE",
            "two": "TWO",
            "six": "SIX",
            "ten": "TEN",
            "list": [1,2,6,10],
            "dist1": {'krushna': 'sybca'} # nested ditionary(diitionry in ditionary)
        } 

print(dict1['key'])
print(dict1['one'])
print(dict1['list'])
print(dict1['dist1']['krushna'])

dict1['one'] = "five" # change the element in ditionary
print(dict1['one'])
