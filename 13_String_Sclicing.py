# String sclicing :-
# that helps to print you a sclice of a string
# it mackes sclice of strings
# sclicing in use as sl = name[starting : Ending]

string = "Krushna"
print(string[0:3])
print(string[3:4])
print(string[4:6])

print(string[-3:-2])
print(string[-2:-6])

# sclicing with the skip value :---->
# we can provide a skip value as a part of our sclice 
# syntax [1:3:2] last index in a string will be skiped
# it's also can use as [0::2]
print(string[0:6:2])
print(string[0::2])

# Amazing tqchniques:---->
print(string[:5]) # is same as print(string[0:5]) {Minimun index of a string}
print(string[2:]) # is same as print(string[2:6]) {Maximum index of a string}
