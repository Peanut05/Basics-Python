# List method :---->
# list method are used to perform many oprations on lists 

# 1) list.sort() :- 
# update list to sequence, it can be number or alphabets

list1 = [7 ,5 ,6 ,8 ,2 , 4, 3, 1, 9]
print(list1)
list1.sort()      # there are sort out origenal list no need  --
print(list1)      # to store into another variable

# list.reverse() :--->
# it reverse list 

list2 = ['a','b','c','d','e','f','g','h']
print(list2)
list2.reverse()
print(list2)

# list.append() :---->
# add or append element at the end of the list
list2.append('i')
print(list2)

# list.insert() :--->
# add element at the place of perfect place
# example :--> list.insert(2 , 3) that add 3 at the index 2

list3 = ['H','D','F','C']
list3.insert(4,'BANK')
print(list3)

# list.pop() :-->
# it delete the element at the index that entered in the pop function

print(list3)
list3.pop(4)
print(list3)

# list.remove() :-->
# remove the element that you enters in the remove function

list4 = ['state','bank','of','india']
print(list4)
list4.remove('india')
print(list4)


