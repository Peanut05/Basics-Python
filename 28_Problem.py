''' Check that a tuple's element cannot be change in python'''
t1 = (1,2,3,4,5,6,6)

t1[0] = 6   # error :--> 'tuple' object does not support item assignment
print(t1) 
