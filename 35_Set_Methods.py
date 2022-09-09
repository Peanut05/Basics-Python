# 1)set.add():--->
# add element in set into the add functio

#a = {1,2,3,4,5,6,7}
#a.add(8)
#a.add(9)
#a.add(0)
#a.add((0,7,7,7,7,7,)) #add tuple
#print(a)

# you can't add list and  into the set cause it mutable/changeable/hashable.
# but you can add tuple in the set its nonmutable.


# 2) len(set) :-->
# it count length of a set (count elements inn set)

#print(len(a))

# 3) set.remove():--->
# remove item in the set that fll up in the emove function.

#a.remove(7) #remove 7 from set a
#print(a) #when value is not present in set throws an error

# 4) set.pop() :--->
# it delete arbitry in the set element and returns that element that removed.

#print(a.pop())
#print(a)

# 5) set.clear() :---> 
# it delete all items in set and make it empty.
#a.clear()
#print(a)

# 6) set.union():--->
# It return a new set with all itemes from both set [union of set]

s1 = {1,2,3,4}
s2 = {4,5,6}
print(s1)
print(s2)
print(s1.union(s2))

# 7) set.intersection() :--->
# Returns a set that contin by both set that is same element in both set

k = s1.intersection(s2)
print(k)
