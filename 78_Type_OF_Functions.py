# Types of function in pyhon :==>>
# 1) Built in function ---alredy present in python
''' Ex.-- range(), len(), print() etc. '''

# 2) User define function --defined by user
''' we create our own function to do some work like privious practice question'''

# Function with Arguments :==>>>

''' A function ca accept some values it can work with.
    we can put this values in a parenthesis a function can also 
    return values as shown below '''

def great(name):
    gr = "Hello ," +name
    return gr 
a = great("prasad") #prasad is passed to greet in name
print(a) # a is containing Hello ,prasad

# ex2.---

def mysum(num1,num2):
    return num1+num2

ss = mysum(11,22)
print(ss)

# Default parameter value :==>>
''' We can have a value as default argument in a function '''

''' if we specify name ='strenger' in the line containg def, 
    this value is used when no arguments are passed. '''

def greatt(name3="stranger"):     #default value is remaining stranger 
    gr = "Hello ," +name3
    return gr 
aa = great("prasad")   #name3 will be "prasad" in the function body
print(aa)
bb = greet()    #name3 "stranger" in function body by default
print(bb)




