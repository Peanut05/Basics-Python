# Tuples method :--->
# Tupels method used for to perform oprations on tuples

# 1) tuple.count(_) :---> 
# That function returns a how much times occurs in a tuple

t1 = (1,2,2,3,4,2,5,5,6,2,7,8,6,1,1)
print(t1)
a = t1.count(5)
b = t1.count(2)
c = t1.count(1)
print(a,b,c)

# tuple.index(_) :--->
# That functin returns the value's index in a tuples
# it's returns first index of an element

d = t1.index(5)
e = t1.index(2)
f = t1.index(1)
print(d,e,f)
